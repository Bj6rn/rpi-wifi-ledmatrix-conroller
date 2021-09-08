#!/usr/bin/python3
#-*- coding: utf-8 -*-
from time import sleep
from signal import pause
from PIL import Image
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT, ATARI_FONT, LCD_FONT
from luma.led_matrix.device import max7219

serial = spi(port=1, device=2, gpio=noop())
device = max7219(serial)

def drawimage(file_path):
    bild = Image.open(file_path)
    bild.load()
    with canvas(device) as draw:
        draw.bitmap((0,0), bild, fill="white")
    
def drawanimation(file_path):
    tileset = Image.open(file_path)
    tileset.load()
    frames = tileset.width//8
    for i in range(frames):
        with canvas(device) as draw:
            x = i*(-8)
            draw.bitmap((x,0), tileset, fill="white")
            sleep(0.2) #5 Bilder pro sekunde

def drawpixelarray(array):
    x = 0
    y = 0
    with canvas(device) as draw:
        for i in range(64):
            if array[i] == 1:
                draw.point((x,y), fill="white")
            else:
                draw.point((x,y), fill="black")
            if (i % 8) == 7:
                x = 0
                y += 1
            else:
                x += 1

def resetmatrix():
    x = 0
    y = 0
    with canvas(device) as draw:
        for i in range(64):
            draw.point((x,y), fill="black")
            if (i % 8) == 7:
                x = 0
                y += 1
            else:
                x += 1
                
def scrollingtext(text):
    show_message(device, text, fill="white", font=proportional(CP437_FONT), scroll_delay=0.075)

if __name__ == "__main__":
    try:
        print("program start (strg+c to end)")
        drawimage("/home/pi/8x8_Pixel-Art/zauberer.png")
        sleep(3)
        x = [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]
        drawpixelarray(x)
        sleep(3)
        scrollingtext("Hallo WELT")
        sleep(1)
        drawanimation("/home/pi/8x8_Pixel-Art/animations/explosion.png")
    except KeyboardInterrupt:
        pass
    finally:
        print("program end")

