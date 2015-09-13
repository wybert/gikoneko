# -*- coding:utf8 -*-
# Author:aisk

import sys
from PIL import Image
import imageio
import progressbar
import numpy as np

WEIGHT = 33
# color = "   ...',;:clodxkO0KXNWMMM"
# color = color[::-1]
color = 'MNHQ$OC?7>!:-;.'

# color = chars

def pic2ascii(image):
    output = ''
    
    size = getsize(image)
    image = image.resize(size)
    image = image.convert('L')
    pixs = image.load()
    for y in range(size[1]):
        for x in range(size[0]):
            output += color[int(pixs[x,y])*(len(color)-1)/255]
        output += '\n'
    return output

def getsize(image):
    '''Calculate the target picture size
    '''
    s_width = image.size[0]
    s_height = image.size[1]
    t_width = WEIGHT
    t_height = (t_width*s_height)/s_width
    t_width = int(t_width * 2.3)
    t_size = (t_width ,t_height)
    return t_size


def viedeo_to_ascii(filename):
    reader = imageio.get_reader(filename)
    frames = []
    bar = progressbar.ProgressBar()

    for im in bar(reader):
        image = Image.fromarray(im)
        frames += [pic2ascii(image)]
    return frames



if __name__ == '__main__':
    # if len(sys.argv) < 2:
    #     print "Useage: pic2ascii.py filename"
    #     sys.exit(1)
    # filename = sys.argv[1]
    # filename = '7.jpg'
    # image = Image.open(filename)
    # print pic2ascii(image)

    filename = 'love_poem.mov'
    frames = viedeo_to_ascii(filename)
    movie ={'name':'love_poem','stop':0.25,'inter':0,'frames':frames}
    np.save('data/movies/love_poem.npy',movie)


