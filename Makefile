all: summaries.json thumbnails

summaries.json: thumbnails
	python imageConvert.py

thumbnails:
	mkdir -p thumbnails

thumbnails.css:
	glue-sprite thumbnails .

thumbnails.png: thumbnails.css
	#An initial version will be created by thumbnails.css
	pngquant 256 thumbnails.png
	mv thumbnails-fs8.png thumbnails.png