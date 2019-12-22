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