from p5 import *

def setup():
    size(500, 500)
    
def draw():
    background(255)
    
    draw_x(200, 200, 100)
    
    draw_x(400, 400, 50)


def draw_x(x, y, line_size):
    stroke(255, 0, 0)
    
    line(x-line_size/2, y-line_size/2, x+line_size/2, y+line_size/2)
    line(x-line_size/2, y+line_size/2, x+line_size/2, y-line_size/2)
    
run()