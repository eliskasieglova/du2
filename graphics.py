from quadtree import _bounding_box
from turtle import mode, speed, forward, backward, right, left, dot, exitonclick, penup, pendown, setup, screensize, goto, setx, sety, setworldcoordinates, setpos

def draw_coords(coords):
    """draws coordinates through Turtle"""
    #speed(10)
    coords.sort(key=lambda c: c[0])  # sorts by x-axis for faster drawing
    new_coords = _recalculate(coords)
    edge, llx, lly, urx, ury = _get_world_coordinates(new_coords)
    setworldcoordinates(llx, lly, urx, ury)  # sets canvas size
    for c in new_coords:
        _go_to_point(c)
    exitonclick()

def _get_world_coordinates(coords):
    """returns points of a rectangle creating boundaries for screen size
    input for function: setworldcoordinates(llx, lly, urx, ury)
    ll --> left lower
    ur --> upper right
    edge --> creates edge
    """
    left_top, right_bottom = _bounding_box(coords)
    edge = 0
    llx = left_top[0]-edge
    lly = right_bottom[1]-edge
    urx = right_bottom [0]+edge
    ury = left_top[1]+edge

    return edge, llx, lly, urx, ury

def _recalculate(coords):
    """recalculates points to make 0,0 in their center for easier and faster drawing"""
    mean = _count_mean(coords)
    coords_recalc = []
    for c in coords:
        c[0] = c[0] - mean[0]
        c[1] = c[1] - mean[1]
        coords_recalc.append((c[0],c[1]))
    print(coords_recalc)
    return coords_recalc

def _count_mean(coords):
    """counts mean latitude and longitude of elements in coords"""
    left_top, right_bottom = _bounding_box(coords)
    mean_x = (left_top[0]+right_bottom[0])/2
    mean_y = (left_top[1]+right_bottom[1])/2
    return (mean_x,mean_y)

def _go_to_point(c):
    """finds path to point and draws dot"""
    penup()
    setx(c[0])
    sety(c[1])
    pendown()
    dot(5,"blue")