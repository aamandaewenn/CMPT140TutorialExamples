from p5 import *

def setup():
    size(400, 400)
    no_stroke()
    global center_x, center_y
    
    center_x = width/2
    center_y = height/2
    
    
def draw():
    # need to always know where the centre is as we move, using a global variable
    global center_x, center_y
    background(255)
    
    # how much we move by
    movement = 10
    
    # define the update based on our key presses
    if key_is_pressed:
        if key == "LEFT":
            center_x -= movement
        elif key == "RIGHT":
            center_x += movement
        elif key == "UP":
            center_y -= movement
        elif key == "DOWN":
            center_y += movement
    
    
    # smallest target point should be based on size of window
    inner_circle_size = min(width, height)/3
    
    # Outermost cirlce
    fill(200, 0, 0)
    circle((center_x, center_y), inner_circle_size)
    
    # Middle white circle
    fill(255)
    circle((center_x, center_y), inner_circle_size*2/3)
    
    # inner cirlce
    fill(200, 0, 0)
    circle((center_x, center_y), inner_circle_size*1/3)
    
run()
