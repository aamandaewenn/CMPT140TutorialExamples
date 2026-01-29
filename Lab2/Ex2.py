from p5 import *

def setup():
    size(400, 400)

def draw():
  # make background blue
  background(0, 0, 255)


  # draw a yellow circle with a red outline up top
  stroke(255, 0, 0)
  fill(255, 255, 0)
  circle(30, 30, 50)

  
  #draw a green rectangle covering the bottom quarter of canvas
  fill(0, 255, 0)
  rect(0, 3*height/4, width, height/4)

    
    
run()