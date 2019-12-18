from quadtree import build_quadtree
from graphics import draw_coords
import json

def load_coordinates(data):
    """loads coordinates from input data and saves them into list"""
    coordinates = []
    for feature in data['features']:
        coord = feature['geometry']['coordinates']
        coordinates.append(coord)
    print(coordinates)
    return coordinates

def convert_to_numbers(list):
    for i in list:
        float(i)
    return

# musime spojit data a zapsat
def append_clusterIDs(data, clusterIDs):
    """appends clusterIDs to coordinates"""
    for feature in data['features']:
        coord = feature['geometry']['coordinates']
        feature['clusterID'] = clusterIDs[(coord[0],coord[1])]
    return data


# load data
with open("input.geojson", "r", encoding="utf-8") as f:
    data = json.load(f)

# list of coordinates converted to float
coordinates = load_coordinates(data)
#coordinates = convert_to_numbers(list_of_coordinates)

# turtle draw coordinates
test_list = [(14.4464198, 50.0790449),(1,1),(0,1),(1,100)]
draw_coords(coordinates)

# returns clusterID for coordinates
clusterIDs = build_quadtree(coordinates)
print(clusterIDs)

# append cluster ID to input data
new_data = append_clusterIDs(data,clusterIDs)

# save data as output.geojson
with open("output.geojson","w",encoding="utf-8") as f:
    json.dump(new_data, f,indent=2, ensure_ascii=False)

