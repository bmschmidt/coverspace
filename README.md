D3 and imagemagick-based dynamic image display

Coverspace came out of the THATCamp New England Session. 



Creating an instance
====================

1. Create an image directory called "images" and fill it with jpgs. (Other imagetypes are trivial to support)
2. Run "make". (Or just execute the one python line in the makefile)
3. Open up index.html on a webserver. (Easy way: `python -m SimpleHTTPServer 8008 &`)
4. Open the page in a web browser, and click around. (For the example: go to http://localhost:8008


Dependencies:
Python wand library
ImageMagick