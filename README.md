D3 and imagemagick-based dynamic image display

Coverspace came out of the THATCamp New England Session. 



Creating an instance
====================

0. Clone this repository (into your webserver directory, if you have one)
1. Create an image directory called "images" and fill it with jpgs. (Other imagetypes are trivial to support)
2. Run "make". (Or just execute the one python line in the makefile)
3. Open up index.html in your browser. (You have to do with a running webserver, unfortunately--the flat file won't load
4. Open the page in a web browser, and click around. (For the example: go to http://localhost:8018)

Creating an instance without a webserver on a Mac:
When in the directory in terminal, just type:
``` {sh}
python -m SimpleHTTPServer 8018 &
open http://localhost:8018
```
Dependencies:
* python w/ wand library
* ImageMagick

Notes
======
Currently, you CAN sort on the filename: so if you make your filenames into something useful (eg datestamps) you can arrange by date.

TODO
====

1. Allow user-generated metadata to be keyed against the filenames (so we can sort by year, for instance.)
1. Incorporate filtering based on metadata.
2. Opacity Slider.
3. grid re-arrangement when both x and y are a single variable. (This will be really cool, actually)
4. Add entropy to the color distribution elements.
5. Think about how subdivisions of the images might be useful for something or other.
4. ???
