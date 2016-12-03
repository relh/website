from PIL import Image 
import os

size = 256,256 

me = Image.open('./me.png')
me.thumbnail(size, Image.ANTIALIAS)
me.save('./mini_wheeee.png')
print "done"
