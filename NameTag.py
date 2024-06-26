import time
import thumby
import math
import os


name="FONZ"

# Letters adopted from
# https://fontstruct.com/fontstructions/show/2240527/31khz-futuristic1412

# BITMAP: width: 16, height: 16
bitmapA = bytearray([
    248,252,14,6,6,6,6,6,6,6,6,6,6,14,252,248,
    127,127,3,3,3,3,3,3,3,3,3,3,3,3,127,127
])

# BITMAP: width: 16, height: 16
bitmapB = bytearray([
    254,254,134,134,134,134,134,134,134,134,134,134,134,206,252,120,
    127,127,97,97,97,97,97,97,97,97,97,97,97,115,63,30
])

# BITMAP: width: 16, height: 16
bitmapC = bytearray([
    248,252,14,6,6,6,6,6,6,6,6,6,6,6,6,6,
    31,63,112,96,96,96,96,96,96,96,96,96,96,96,96,96
])

# BITMAP: width: 16, height: 16
bitmapD = bytearray([
    254,254,6,6,6,6,6,6,6,6,6,6,6,14,252,248,
    127,127,96,96,96,96,96,96,96,96,96,96,96,112,63,31
])

# BITMAP: width: 16, height: 16
bitmapE = bytearray([
    254,254,134,134,134,134,134,134,134,134,134,134,134,134,6,6,
    127,127,97,97,97,97,97,97,97,97,97,97,97,97,96,96
])

# BITMAP: width: 16, height: 16
bitmapF = bytearray([
    254,254,134,134,134,134,134,134,134,134,134,134,134,134,6,6,
    127,127,1,1,1,1,1,1,1,1,1,1,1,1,0,0
])

# BITMAP: width: 16, height: 16
bitmapG = bytearray([
    248,252,14,6,6,6,6,6,134,134,134,134,134,134,134,134,
    31,63,112,96,96,96,96,96,97,97,97,97,97,97,127,127
])

# BITMAP: width: 16, height: 16
bitmapH = bytearray([
    254,254,128,128,128,128,128,128,128,128,128,128,128,128,254,254,
    127,127,1,1,1,1,1,1,1,1,1,1,1,1,127,127
])

# BITMAP: width: 16, height: 16
bitmapI = bytearray([
    6,6,6,6,6,6,6,254,254,6,6,6,6,6,6,6,
    96,96,96,96,96,96,96,127,127,96,96,96,96,96,96,96
])
          
# BITMAP: width: 16, height: 16
bitmapJ = bytearray([
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,254,254,
    30,62,112,96,96,96,96,96,96,96,96,96,96,112,63,31
])

# BITMAP: width: 16, height: 16
bitmapK = bytearray([
    254,254,128,128,128,128,128,128,128,128,128,192,224,112,62,30,
    127,127,1,1,1,1,1,1,1,1,1,3,7,14,124,120
])
        
# BITMAP: width: 16, height: 16
bitmapL = bytearray([
    254,254,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    127,127,96,96,96,96,96,96,96,96,96,96,96,96,96,96
])
            
# BITMAP: width: 16, height: 16
bitmapM = bytearray([
    254,254,14,28,56,112,224,192,192,224,112,56,28,14,254,254,
    127,127,0,0,0,0,0,1,1,0,0,0,0,0,127,127
])

# BITMAP: width: 16, height: 16
bitmapN = bytearray([
    254,254,14,28,56,112,224,192,128,0,0,0,0,0,254,254,
    127,127,0,0,0,0,0,1,3,7,14,28,56,112,127,127
])
            
# BITMAP: width: 16, height: 16
bitmapO = bytearray([
    248,252,14,6,6,6,6,6,6,6,6,6,6,14,252,248,
    31,63,112,96,96,96,96,96,96,96,96,96,96,112,63,31
])
            
# BITMAP: width: 16, height: 16
bitmapP = bytearray([
    254,254,134,134,134,134,134,134,134,134,134,134,134,206,252,120,
    127,127,1,1,1,1,1,1,1,1,1,1,1,1,0,0
])
            
# BITMAP: width: 16, height: 16
bitmapQ = bytearray([
    248,252,14,6,6,6,6,6,6,6,6,6,6,14,252,248,
    31,63,112,96,96,96,96,96,96,96,96,108,124,56,127,111
])

# BITMAP: width: 16, height: 16
bitmapR = bytearray([
    254,254,134,134,134,134,134,134,134,134,134,134,134,206,252,120,
    127,127,1,1,1,1,1,1,1,1,1,1,3,7,126,124
])

# BITMAP: width: 16, height: 16
bitmapS = bytearray([
    120,252,206,134,134,134,134,134,134,134,134,134,134,134,6,6,
    96,96,97,97,97,97,97,97,97,97,97,97,97,115,63,30
])

# BITMAP: width: 16, height: 16
bitmapT = bytearray([
    6,6,6,6,6,6,6,254,254,6,6,6,6,6,6,6,
    0,0,0,0,0,0,0,127,127,0,0,0,0,0,0,0
])

# BITMAP: width: 16, height: 16
bitmapU = bytearray([
    254,254,0,0,0,0,0,0,0,0,0,0,0,0,254,254,
    31,63,112,96,96,96,96,96,96,96,96,96,96,112,63,31
])

# BITMAP: width: 16, height: 16
bitmapV = bytearray([
    14,62,248,224,128,0,0,0,0,0,0,128,224,248,62,14,
    0,0,0,3,15,62,120,96,96,120,62,15,3,0,0,0
])
            
# BITMAP: width: 16, height: 16
bitmapW = bytearray([
    254,254,0,0,0,0,0,128,128,0,0,0,0,0,254,254,
    127,127,112,56,28,14,7,3,3,7,14,28,56,112,127,127
])
            
# BITMAP: width: 16, height: 16
bitmapX = bytearray([
    6,14,28,56,112,224,192,128,128,192,224,112,56,28,14,6,
    96,112,56,28,14,7,3,1,1,3,7,14,28,56,112,96
])
            
# BITMAP: width: 16, height: 16
bitmapY = bytearray([
    6,14,28,56,112,224,192,128,128,192,224,112,56,28,14,6,
    0,0,0,0,0,0,1,255,255,1,0,0,0,0,0,0
])
            
# BITMAP: width: 16, height: 16
bitmapZ = bytearray([
    6,6,6,6,6,134,134,134,134,134,198,230,118,62,30,14,
    112,120,124,110,103,99,97,97,97,97,97,96,96,96,96,96
])

bitmapHeart = bytearray([
    0,248,4,2,2,4,4,8,8,4,4,114,114,4,248,0,
    0,0,3,4,8,16,32,64,64,32,16,8,4,3,0,0
])

letterBitmapAssignment = {
    "A": bitmapA, "B": bitmapB, "C": bitmapC,
    "D": bitmapD, "E": bitmapE, "F": bitmapF,
    "G": bitmapG, "H": bitmapH, "I": bitmapI,
    "J": bitmapJ, "K": bitmapK, "L": bitmapL,
    "M": bitmapM, "N": bitmapN, "O": bitmapO,
    "P": bitmapP, "Q": bitmapQ, "R": bitmapR,
    "S": bitmapS, "T": bitmapT, "U": bitmapU,
    "V": bitmapV, "W": bitmapW, "X": bitmapX,
    "Y": bitmapY, "Z": bitmapZ, "h": bitmapHeart
}

def concatLettersToBitmap(name):
    name_list=list(name)
    bitmap_list = [letterBitmapAssignment[letter] for letter in name_list]
    bitmap_list_lists = [list(bl) for bl in bitmap_list]
    first_rows = [bl[0:16] for bl in bitmap_list_lists]
    second_rows = [bl[16:32] for bl in bitmap_list_lists]

    result = []
    for first_row in first_rows:
        result.extend(first_row)
        result.extend([0])
    for second_row in second_rows:
        result.extend(second_row)
        result.extend([0])

    return result

def half_len(lst):
    return int(len(lst)/2)

def create16BitSprite(pixels):
    width = half_len(pixels)
    return thumby.Sprite(width, 16, bytearray(pixels), 0, 0)

def sliceBitmap(pixels):
    result = []
    half = half_len(pixels)
    for i in range(half):
        result.append(create16BitSprite([pixels[i], pixels[i+half]]))
    return result

class Scroller:
    def __init__(self, tickFn, ticks_per_letter=30, vertical_positioning=lambda t, i, h: 0):
        self.tickFn = tickFn
        self.initTime = tickFn()
        self.velocity = 1/ticks_per_letter
        self.vertical_positioning = vertical_positioning

    def scroll(self, sprites):
        relativeTick = self.tickFn() - self.initTime
        distance = 0
        for i in range(len(sprites)):
            sprite = sprites[i]
            sprite.x = (thumby.display.width+1) - math.floor(relativeTick*self.velocity) + distance
            sprite.y = self.vertical_positioning(relativeTick, i, sprite.height)
            distance = distance + sprite.width
            isLastSprite = (i == (len(sprites)-1))
            spriteLeavesScreenLeft = (sprite.x < (sprite.width * -1))
            thumby.display.drawSprite(sprite)
            if isLastSprite and spriteLeavesScreenLeft:
                return True


def wave(tick, i, height):

    t0 = tick+i*10

    bobRate = 250 # Set arbitrary bob rate (higher is slower)
    bobRange = (height)/2  # How many pixels to move the sprite up/down (-5px ~ 5px)

    # Calculate number of pixels to offset sprite for bob animation
    bobOffset = math.sin(t0 / bobRate) * bobRange
    return int(round((thumby.display.height/2) - (height/2) + bobOffset))



mode = "thumby"
if (hasattr(os, "getenv")):
    mode = os.getenv("THMB_MODE")

def thumby_mode():
    print("RUNNING THUMBY")
    gap = len(name)*1
    print("Display \""+name+"\" as "+str(len(name)*16+gap)+"x16 bitmap")
    bitmap0 = bytearray(concatLettersToBitmap(name))

    thumbySprites = sliceBitmap(bitmap0)

    # Set the FPS (without this call, the default fps is 30)
    thumby.display.setFPS(60)
    scroller = Scroller(time.ticks_ms, 27, wave)

    while(1):
        thumby.display.fill(0)
        if scroller.scroll(thumbySprites):
            break

        thumby.display.update()

    return

def pc_mode():
    print("RUNNING PC")
    return

def main():
    if (mode == "thumby"):
        thumby_mode()
        return
    else:
        pc_mode()

main()