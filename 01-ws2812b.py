#!/usr/bin/python3

import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18,1)

def wheel(pos):
  if pos <0 or pos > 255:
    r = g = b = 0 
  elif pos < 85:
    r = int(pos*3)
    g = int(255 - pos * 3)
    b = 0
  elif pos < 170:
    pos -= 85
    r = int(255 - pos * 3)
    g = 0
    b = int(pos * 3)
  else:
    pos -= 170
    r = 0
    g = int(pos * 3)
    b = int(255 - pos * 3)
  return (r, g, b)

while True:
  for j in range(255):
    pixels[0] = wheel(j)
    pixels.show()
    time.sleep(0.01)

#while True:
#  pixels[0] = (255,0,0) # RED
#  time.sleep(1)
#  pixels[0] = (0,255,0) # GREEN
#  time.sleep(1)
#  pixels[0] = (0,0,255) # BLUE

