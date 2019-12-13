from quadtree import build_quadtree
import json

def load_coordinates(data):
    """loads coordinates from imput data and saves them into list"""
    coordinates = []
    for feature in data['features']:
        coord = feature['geometry']['coordinates']
        coordinates.append(coord)
    print(coordinates)
    return coordinates

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

# list of coordinates
coordinates = load_coordinates(data)

# returns clusterID for coordinates
clusterIDs = build_quadtree(coordinates)
print(clusterIDs)

# append cluster ID to input data
new_data = append_clusterIDs(data,clusterIDs)

# save data as output.geojson
with open("output.geojson","w",encoding="utf-8") as f:
    json.dump(new_data, f,indent=2, ensure_ascii=False)