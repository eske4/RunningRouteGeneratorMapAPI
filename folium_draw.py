import folium
from PIL import Image

import pdfkit
import fitz

from haversine import haversine


def create_map(coords, poiscoords, homecoord, startcoord):
    home = folium.features.CustomIcon('House.png', icon_size=(75, 75))
    start = folium.features.CustomIcon('flag.png', icon_size=(75, 75))
    poi = folium.features.CustomIcon('poi.png', icon_size=(75, 75))
    # calculate the center of the map and the appropriate zoom level to fit all coordinates
    center = [sum([coord[0] for coord in coords]) / len(coords), sum([coord[1] for coord in coords]) / len(coords)]

    # create a Folium map centered on the calculated center with the appropriate zoom level
    m = folium.Map(location=center, height=800, width=800, zoom_start=15, zoom_control=True,
               scrollWheelZoom=True, dragging=True, no_touch=False, center=center)

    dist = haversine(homecoord, startcoord, unit='m')

    if dist <= 100:
        startcoord = homecoord

    if startcoord == homecoord:
        folium.Marker(location=homecoord, icon=home).add_to(m)
    else:
        folium.Marker(location=startcoord, icon=start).add_to(m)
        folium.Marker(location=homecoord, icon=home).add_to(m)

    coords.insert(0, startcoord)
    coords.append(homecoord)
    # add a polyline to the map connecting all the coordinates in the list
    folium.PolyLine(coords, color='blue').add_to(m)

    # add markers to the map at each coordinate in the list
    poiscoords.pop(-1)
    if poiscoords[-1] == homecoord:
        poiscoords.pop(-1)

    # add markers to the map for each POI coordinate
    for poicoords in poiscoords:
        folium.Marker(location=poicoords).add_to(m)

    # calculate the bounds of the map
    bounds = [[min([coord[0] for coord in coords]), min([coord[1] for coord in coords])],
          [max([coord[0] for coord in coords]), max([coord[1] for coord in coords])]]

    # define the margin in terms of latitude and longitude
    lat_margin = 0.0010  # adjust this value as needed
    lon_margin = 0.0010  # adjust this value as needed

    # add the margin to the bounds
    bounds_with_margin = [[bounds[0][0] - lat_margin, bounds[0][1] - lon_margin],
            [bounds[1][0] + lat_margin, bounds[1][1] + lon_margin]]

    # pass the modified bounds to fit_bounds()
    m.fit_bounds(bounds_with_margin)

    # set the size of the map
    m._size = (500, 500)

    return m

def convert_map_png(folium_map, file_name):
    mapName = file_name

    # Get HTML File of Map
    folium_map.save(mapName + '.html')
    htmlfile = mapName + '.html'

    # Convert Map from HTML to PDF, Delay to Allow Rendering
    options = {
        'javascript-delay': 500,
        'page-size': 'Letter',
        'page-width': '500px',
        'page-height': '500px',
        'margin-top': '0.0in',
        'margin-right': '0.0in',
        'margin-bottom': '0.0in',
        'margin-left': '0.0in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ]
    }
    pdfkit.from_file(htmlfile, (mapName + '.pdf'), options=options)
    pdffile = mapName + '.pdf'

    # Convert Map from PDF to PNG
    doc = fitz.open(pdffile)
    page = doc.load_page(0)
    pix = page.get_pixmap()
    output = mapName + '.png'
    pix.save(output)
    pngfile = mapName + '.png'
    doc.close()

    return Image.open(output)
