from p5 import *

def setup():
    size(400, 400)
    no_stroke()
    
def draw():
    background(255)
    
    # find the center of the window
    center_x = width/2
    center_y = height/2
    
    
    # smallest target point should be based on size of window
    inner_circle_size = min(width, height)/3
    
    
    # Outermost cirlce
    fill(200, 0, 0)
    circle(center_x, center_y, inner_circle_size*3)
    
    # Middle white circle
    fill(255)
    circle(center_x, center_y, inner_circle_size*2)
    
    # inner cirlce
    fill(200, 0, 0)
    circle(center_x, center_y, inner_circle_size)
    
    
run()