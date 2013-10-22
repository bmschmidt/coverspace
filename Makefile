all: summaries.json thumbnails

summaries.json: thumbnails
	python imageConvert.py

thumbnails:
	mkdir -p thumbnails
