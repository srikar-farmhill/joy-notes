from joy import *
from ipywidgets import interact, IntSlider, FloatSlider

def ellipse_star(n):
    return ellipse(w=150, h=75)|repeat(n, rotate(180/n))

def beside(s1, s2):
    s1 = s1 | scale(x=0.5) | translate(x=-75)
    s2 = s2 | scale(x=0.5) | translate(x=75)    
    return s1+s2

def below(s1, s2):
    s1 = s1 | scale(y=0.5) | translate(y=75)
    s2 = s2 | scale(y=0.5) | translate(y=-75)    
    return s1+s2

def grid(s1, s2, s3, s4):
    return below(
        beside(s1, s2),
        beside(s3, s4))

def random_circles(r=125, n=10):
    shapes = [circle(r=random(r)) for i in range(n)]
    return combine(shapes)

def square(w):
    """
    Creates a rectangle with a given width, and height equal to the given width.

    Example:

    square(100)
    Gives a rectangle with width=100, and height equal to width that is, equal to 100.
    """
    return rectangle(w=w, h=w)

def random_squares(w=250, n=15):
    shapes = [square(w=random(w)) for i in range(n)]
    return combine(shapes)

def repeat4(shape):
    return grid(shape, shape, shape, shape)

def grid_1(shape_maker):
    return grid(shape_maker(), shape_maker(), shape_maker(), shape_maker())

def grid_2(shape_maker):
    def grid_maker():
        return grid_1(shape_maker)
    return grid_1(grid_maker)

def grid_3(shape_maker):
    def grid_maker():
        return grid_1(shape_maker)
    return grid_2(grid_maker)

def concentric_circles(radius, n):
    delta = radius/n
    circles = [circle(r=i*delta) for i in range(1, n+1)]
    return combine(circles)

def bcircle(bx=0, by=0, r=50):
    cx = bx
    cy = by+r
    return circle(x=cx, y=cy, r=r)

def conbottomic_circles(r, n):
    shift = r/n
    design = [bcircle(r=i*shift) for i in range(1, n+1)]
    return combine(design)|translate(y=-r)

def row(shapes):
    n=len(shapes)
    dx=300/n
    offset=-150 + dx/2
    new_shapes=[shapes[i]|scale(1/n)|translate(x=dx*i) for i in range(n)]
    return combine(new_shapes)|translate(x=offset)

def sigma(n):
    return sum(range(1, n+1))

def lcircle(x, y, r):
    cx = x+r
    cy = y
    c = circle(x=cx, y=cy, r=r)
    return c

def rcircle(x, y, r):
    cx = x-r
    cy = y
    c = circle(x=cx, y=cy, r=r)
    return c

def left_touching_circles(n):
    r0 = 150/sigma(n)
    x = -150
    y = 0
    r = r0
    shapes = []
    for i in range(n):
        c = lcircle(x, y, r)
        x = x+2*r
        y = 0
        r = r+r0
        shapes.append(c)
    return combine(shapes)

def right_touching_circles(n):
    r0 = 150/sigma(n)
    x = 150
    y = 0
    r = r0
    circles = []
    for i in range(n):
        c = rcircle(x, y, r)
        x = x-2*r
        y = 0
        r = r+r0
        circles.append(c)
    return combine(circles)

def donut(x, y, r):
    a = circle(x=x, y=y, r=r)
    b = circle(x=x, y=y, r=r/2)
    return a+b

def donut_grid(n):
    size = 300/n
    r = size/2
    x = -150+r
    y = -150+r
    shapes = []
    for j in range(n):
        for i in range(n):
            c = donut(x, y, r)
            shapes.append(c)
            x = x+size
        y = y+size
        x = -150+r
    return combine(shapes)

def random_squares_grid(n):
    size = 300/n
    r = size/2
    x = -150+r
    y = -150+r
    shapes = []
    for j in range(n):
        for i in range(n):
            c = random_squares(w=size, n=10)|translate(x=x, y=y)
            shapes.append(c)
            x = x+size
        y = y+size
        x = -150+r
    return combine(shapes)

def super_grid(shape_maker, n):
    size = 300/n
    r = size/2
    x = -150+r
    y = -150+r
    shapes = []
    for j in range(n):
        for i in range(n):
            c = shape_maker(size)|translate(x=x, y=y)
            shapes.append(c)
            x = x+size
        y = y+size
        x = -150+r
    return combine(shapes)