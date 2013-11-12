import os
import json
import re

files = json.loads(open("owi.json").read())

outputFile = open("metadata.json","w")
outputs = []

for file in files:
    loc = dict()
    loc['entropy'] = file['entropy']
    loc['url'] = file['locpermalink']
    loc['photographer'] = file['photographer']
    loc['state'] = file['state']
    loc['year'] = file['year']
    file['thumbnail'] = re.sub("r","",file["thumbnail"])
    loc['filename'] = file['thumbnail'] + "_150px" + ".jpg"
    outputs.append(loc)
    
outputFile.write(json.dumps(outputs))
