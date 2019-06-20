# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import os

def main():
    os.chdir(r'C:\\Users\Leo Wang\Desktop')
    image = Image.open('headShot.jpg')
    draw = ImageDraw.Draw(image)
    width, height = image.size
    font = ImageFont.truetype('C:\\Windows\Fonts\Calibri.ttf',200)
    draw.text((width - 300, 0), '99+', 'Red', font)
    image.show()
    image.save('newHeadShot.jpg')







if __name__ == '__main__':
    main()