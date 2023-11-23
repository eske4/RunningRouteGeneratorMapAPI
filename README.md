# RunningRouteGeneratorMapAPI
An map image generator for the university project

This api purpose is to draw an map to illustrate the route.
an example can be seen below
<img src="https://github.com/eske4/RunningRouteGeneratorMapAPI/blob/main/Images/DrawMap.png" width="500">

API endpoint

/DrawMap/<coords>/<poicoords>/<homecoord>/<startcoord>

Takes the coordinates that draws the lines, point of interest coordinates to draw markers of where the pois are a home coordinate to mark the end destination and a start coordinate a marker for where you start



Setup example

1. Create a PythonAnywhere account [here](https://www.pythonanywhere.com)
2. Upload the files from this repository and run the server with flask_app

