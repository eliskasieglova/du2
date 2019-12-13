from turtle import forward, right, left

# global variables
clusterID=0
coord_clusterID = {} # dictionary of coordinates and their cluster IDs

def build_quadtree(coords):
    """finds edges of bounding box and calls recursive function"""
    global coord_clusterID
    global clusterID
    clusterID = 0
    coord_clusterID = { }
    # create boundaries of bounding box
    left_top, right_bottom = bounding_box(coords)
    # recursive function
    _build(coords, left_top, right_bottom)
    return coord_clusterID

def bounding_box(coords):
    """finds edges of bounding box"""
    min_x = min(coords, key = lambda p: p[0])[0]
    min_y = min(coords, key = lambda p: p[1])[1]
    max_x = max(coords, key = lambda p: p[0])[0]
    max_y = max(coords, key = lambda p: p[1])[1]
    print(min_x)
    print(min_y)
    print(max_x)
    print(max_y)
    return (min_x, max_y), (max_x, min_y)


def _build(coords, left_top, right_bottom):
    """
    1. Divide the current two dimensional space into four boxes.
    2. If a box contains one or more points in it, create a child object, storing in it the two dimensional space of the box
    3. If a box does not contain any points, do not create a child for it
    4. Recurse for each of the children.
    """
    if len(coords) < 5:
        global clusterID
        global coord_clusterID
        for c in coords:
            coord_clusterID[(c[0],c[1])] = clusterID
        clusterID += 1
        return
    else:
        # points of net for each bounding box created after recurse
        a1 = left_top
        a2 = ((right_bottom[0] + left_top[0]) / 2, left_top[1])
        a3 = (left_top[0], (right_bottom[1] + left_top[1]) / 2)
        a4 = ((right_bottom[0] + left_top[0]) / 2, (right_bottom[1] + left_top[1]) / 2)
        b1 = a4
        b2 = (right_bottom[0], (right_bottom[1] + left_top[1]) / 2)
        b3 = ((right_bottom[0] + left_top[0]) / 2, right_bottom[1])
        b4 = right_bottom

        # empty lists for each sub-box
        l1 = []
        l2 = []
        l3 = []
        l4 = []

        for c in coords:
            if inside_box(c, a1, b1):
                l1.append(c)
            elif inside_box(c, a2, b2):
                l2.append(c)
            elif inside_box(c, a3, b3):
                l3.append(c)
            elif inside_box(c, a4, b4):
                l4.append(c)
        # recurse
        _build(l1, a1, b1)
        _build(l2, a2, b2)
        _build(l3, a3, b3)
        _build(l4, b1, b4)

def inside_box(point, min, max):
    """decides if point is inside bounding box"""
    if point[0] >= min[0] and point[0] <= max[0] and point[1] >= max[1] and point[1] <= min[1]:
        return True
    else:
        return False
