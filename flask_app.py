
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, send_file

import io
import sys

print(sys.path)
from scripts import folium_draw as fd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/DrawMap/<coords>/<poicoords>/<homecoord>/<startcoord>/')
@app.route('/DrawMap/<coords>/<poicoords>/<homecoord>/<startcoord>')
def send_img(coords, poicoords, homecoord, startcoord):
    coords_list = [float(coord) for coord in coords.split(',')]
    coords_pairs = [(coords_list[i], coords_list[i+1]) for i in range(0, len(coords_list), 2)]

    poicoords_list = [float(coord) for coord in poicoords.split(',')]
    poicoords_pairs = [(poicoords_list[i], poicoords_list[i+1]) for i in range(0, len(poicoords_list), 2)]

    homecoord_pair = tuple(map(float, homecoord.split(',')))
    startcoord_pair = tuple(map(float, startcoord.split(',')))

    m = fd.create_map(coords_pairs, poicoords_pairs, homecoord_pair, startcoord_pair)

    # convert the map to PNG
    map_png = fd.convert_map_png(m, 'image')

    # create a file-like object to send the PNG image data
    img_io = io.BytesIO()
    map_png.save(img_io, 'PNG')
    img_io.seek(0)

    # send the PNG image data as a file
    return send_file(img_io, mimetype='image/png')


