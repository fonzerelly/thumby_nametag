class Display:
  def __init__(self):
    self.width = 72
    self.height = 40

display = Display()

class Sprite:
  def __init__(self, width, height, bitmapData, x=0, y=0, key=0, mirrorX=0, mirrorY=0):
    self.x = x
    self.y = y
    self.width = width
    self.height = height

  
