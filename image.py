from lib2to3.pytree import convert
import os
from PIL import Image, ImageFilter

#The path of the current dir for saving files
curpath = os.path.dirname(__file__)

img = Image.open(curpath + r'\astro.jpg')
img.thumbnail((200, 250))


filename = 'thumbnail'
format = 'png'
pathname = curpath + "\\" + filename + '.' + format
img.save(pathname, format)

