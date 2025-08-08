from p5 import *

def setup():
  createCanvas(500,500)
  rectMode(CENTER)
  
def draw():
  background("black")
  drawTickAxes()
  size = 50
  
  for i in range(10):#rows
    for j in range(10) : #columns
      x = size/2 + i*size
      y = size/2 + j*size

      if (i+j) % 2 ==0:
        fill("#FF1493")
      else:
        fill("white")
        
      push() 
      translate(x,y)
      rotate(mouseX)
      scale(mouseY/100)
      square(0,0,size)
      pop()
