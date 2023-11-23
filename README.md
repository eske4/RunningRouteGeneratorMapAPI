# RunningRouteGeneratorMapAPI

**Description:**
RunningRouteGeneratorMapAPI is a map image generator developed for a university project. The primary objective of this API is to visually represent running routes by drawing maps. An example of the generated map is displayed below:

![Drawn Map](https://github.com/eske4/RunningRouteGeneratorMapAPI/blob/main/Images/DrawMap.png)

**API Endpoint:**

`/DrawMap/[coords]/[poicoords]/[homecoord]/[startcoord]`

This endpoint takes various coordinates to draw lines, markers for points of interest (POIs), a marker for the end destination (home coordinate), and a marker for the starting point.

- `[coords]`: Coordinates for drawing the route lines.
- `[poicoords]`: Coordinates for drawing markers at points of interest (POIs).
- `[homecoord]`: Coordinates for marking the end destination.
- `[startcoord]`: Coordinates for marking the starting point.

**Setup Example:**

1. Create a PythonAnywhere account [here](https://www.pythonanywhere.com).
2. Upload the files from this repository and run the server using `flask_app`.

This setup example assumes the usage of PythonAnywhere as the hosting platform. Ensure that you have the necessary dependencies installed and follow the provided example to deploy the RunningRouteGeneratorMapAPI.

**Note:** The process for setting up and running the API may have changed due to updates in the Python packages used. Ensure you have the latest dependencies installed, and consult the [GitHub repository](https://github.com/eske4/RunningRouteGeneratorMapAPI) for any updated instructions or changes to the setup process.
