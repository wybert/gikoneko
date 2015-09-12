### --- encoding: utf-8 ---
#author:happybeetle

# def emoji(emo):
import json
import chardet
import sys 
import random
import numpy as np 

try:
    emojis = json.load(open("data/emoji.json",'r'))
    emoticons = json.load(open("data/emoticons.json",'r'))
    myfavorites = np.load('data/myfavorites.npy').item()
except Exception,e:
    print str(e)
    print "Could not open emoji file "
    sys.exit(1)

gikoneko=myfavorites['gikoneko']
def all_my_favorites():    
    for k,v in myfavorites.iteritems():
        print k
gikoneko=myfavorites['gikoneko']
def gikoneko_all():
    for i,item in enumerate(gikoneko):
        print i,item %('')  
def random_gikoneko_say(something):
    print gikoneko[random.randint(0,len(gikoneko)-1)]%(u'＜ '+something) 
def random_gikoneko():
    print gikoneko[random.randint(0,len(gikoneko)-1)]
def gikoneko_say(i,something):
    print gikoneko[i]%(u'＜ '+something)

def gikoneko_select(i):
    print gikoneko[i]%(u'')
