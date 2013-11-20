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
        self.statistics = {"filename":imageDirectory +"/" + filename,"id":filename,"thumbnail":"thumbnails/" + filename}
        try:
            self.img = Image(filename=self.statistics['filename'])
        except:
            sys.stderr.write("Warning: imageMagick couldn't load " + self.statistics["filename"]+ "\n")
            pass


    def writeThumbnails(self):
        try:
            with self.img.clone() as i:
                #Resize so the largest dimension is 100px wide.
                if i.height > i.width and i.height > 100:
                    i.transform(resize='x100')
                elif i.width > 100:
                    i.transform(resize='100x')
                else:
                    pass

                self.thumbnail = i.clone()
                i.save(filename=self.statistics["thumbnail"])
        except:
            pass
            
    def averages(self):
        self.writeThumbnails()
        try:
            img = self.thumbnail
            #It's faster to do the reconversion from the thumbnail than the original.
        except:
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
    
    
def image_entropy(im):
    """
    From http://stackoverflow.com/questions/1516736/django-sorl-thumbnail-crop-picture-head
    From Reddit: Calculate the entropy of an image"""
    hist = im.histogram()
    hist_size = sum(hist)
    hist = [float(h) / hist_size for h in hist]
    return -sum([p * math.log(p, 2) for p in hist if p != 0])


def writeOutJSON(): 
    #An array which d3 will use to store image statistics
    stats = []
    
    try:
        files = os.listdir(imageDirectory)

    except:
        print "Have you created a folder called images and filled it with JPGs?"
        raise

    for filename in files:
        #Update the screen w/ a ticker.
        sys.stdout.write( filename + "\r")
        averages = myFile(filename).averages()
        stats.append(averages)

    summaries.write(json.dumps(stats))

if __name__=="__main__":
    writeOutJSON()
