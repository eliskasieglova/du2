from quadtree import build_quadtree
import json

def load_coordinates(data):
    coordinates = []
    for i in data['features']:
        coord = i['geometry']['coordinates']
        coordinates.append(coord)
    print(coordinates)
    return coordinates




#nactu data
with open("data.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)

# list of coordinates
coordinates = load_coordinates(data)

# vytvorime quad tree v quadtree.py a zavolame ho tady, vraci neco z ceho vycteme clusterID pro kazdou coordinate
clusterIDs = build_quadtree(coordinates)
print(clusterIDs)

# musime spojit data a zapsat
def append_clusterIDs(data, clusterIDs)


# ulozime data