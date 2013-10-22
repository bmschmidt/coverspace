import urllib2
from BeautifulSoup import BeautifulSoup
import re
import json
import os
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

output = open("TimeCovers.txt",'a')

class timePage:
    def __init__(self,url):
        self.url = url


    def setup(self):
        """
        There turns out actually to be quite a good deal of 
        metadata that we can work with on all of these. Credits, etc.
        """
        page = urllib2.urlopen(self.url)
        self.soup = BeautifulSoup(page.read())
        self.metadata = {}
        try:
            self.img = self.soup.find("img",attrs={"width":"400"})
            self.imgLink = self.img.get('src')
        except AttributeError: #One Page does this wrong, so I'm excepting it.
            self.img = self.soup.find("img")
            self.imgLink = self.img.get("src")

        self.metadata["imgCaption"] = self.img.get('title')
        credit = self.soup.find("div",text =re.compile("Cover Credit"))
        try:
            self.metadata["credit"] = re.sub("Cover Credit: ","",credit)
        except:
            self.metadata["credit"] = ""

        self.metadata["date"] = re.sub(r".*(\d\d\d\d)(\d\d)(\d\d).*",r"\1-\2-\3",self.url)
        self.metadata["year"] = self.metadata["date"][:4]
        self.metadata["url"] = self.url
        self.metadata["imageUrl"] = self.imgLink
        #Get keywords
        self.metadata["keywords"] = self.soup.findAll("meta",attrs={"name":"keywords"})[0].get("content").split(",")

        #Get next link
        self.nextUp = "http://content.time.com/" + self.soup.findAll("span",attrs={"class":"next"})[0].find("a").get("href")

    def download(self):
        if not (os.path.exists("images/" + self.metadata["date"] + ".jpg")):
            link = urllib2.Request(self.imgLink,headers=headers)
            jpg = open("images/" + self.metadata["date"] + ".jpg","w")
            jpg.write(urllib2.urlopen(link).read())
            jpg.close()
            return True
        return False

    def writeMetadata(self):
        output.write(json.dumps(self.metadata) + "\n")
        
if __name__ == "__main__":
    start = "http://content.time.com//time/covers/0,16641,19310921,00.html"
    while True:
        print start + "\r"
        file = timePage(start)
        file.setup()
        if file.download():
            """
            Only write the metadata if it returns that it's
            downloading for the first time.
            """
            file.writeMetadata()
            
        start = file.nextUp

