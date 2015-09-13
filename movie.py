#!/usr/bin/env python
# -*- coding=utf-8 -*-
#Using GPL v2
"""
Usage:
Just A Template
"""
# import time
from __future__ import division
import sys,time,os
import numpy as np

movies={}
for file_str in os.listdir('data/movies'):
    # print file_str
    # print file_str.strip('.npy')
    movies[file_str.split('.')[0]] = np.load('data/movies/'+file_str).item()

# movies = np.load('movies.npy').item()
# print test
# movies =test.items()


def screen_clear():
    print '\n'*70
    # os.system('clear')
    # pass

def play_movie_by_name(name,start_title = 0,end_title = 0): 
    
    movie = movies[name]
    screen_clear()
    # if start_title == 0:
    #     print ' '*4 + movie['name']
    # else:
    #     print start_title
    # time.sleep(1)
    # screen_clear()
    time.sleep(1)
    for frame in movie['frames']:
        print frame
        time.sleep(movie['stop'])
        screen_clear()
        time.sleep(movie['inter'])
    time.sleep(1)
    # if end_title == 0:
    #     print '              the     end              '
    # else:
    #     print end_title
    # time.sleep(1)

def list_all_movies():

    for item in movies.iterkeys():
        print item

if __name__ =='__main__':
    list_all_movies()
    # play_movie_by_name('love_story')
    play_movie_by_name('love_movie')

    # 