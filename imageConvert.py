#!/usr/bin/python

from wand.image import *
from wand.color import *
import colorsys
import os
import json
import sys

summaries = open("summaries.json","w")

#You have to store the images all in one directory
imageDirectory = "images"

class myFile:
    def __init__(self,filename="1987-01-01.jpg"):
        self.statistics = {"filename":imageDirectory +"/" + filename}
        try:
            self.img = Image(filename=self.statistics['filename'])
        except:
            pass
            
    def averages(self):
        try:
            img = self.img
        except:
            sys.stderr.write("Warning: imageMagick couldn't load " + self.statistics["filename"]+ "\n")
            return dict()
        img.resize(1,1)
        average = img[0,0]
        rgb = (average.red,average.green,average.blue)
        hsv = colorsys.rgb_to_hsv(*rgb)
        yiq = colorsys.rgb_to_yiq(*rgb)
        hls = colorsys.rgb_to_hls(*rgb)
        
        spaces = ["rgb","hsv","yiq","hls"]

        for space in spaces:
            for n in range(len(space)):
                self.statistics[space + "_" + space[n]] = eval(space)[n] 
                #Creates a dictionary with keys like "rgb_r":255

        return self.statistics
    
    
def writeOutJSON(): 
    stats = []
    
    try:
        files = os.listdir(imageDirectory)
    except:
        print "Have you created a folder called images and filled it with JPGs?"
        raise

    for filename in files:
        sys.stdout.write( filename + "\r")
        averages = myFile(filename).averages()
        stats.append(averages)

    summaries.write(json.dumps(stats))

writeOutJSON()
