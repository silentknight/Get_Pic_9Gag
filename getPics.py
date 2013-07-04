#!/usr/bin/python

import time
import urllib2
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):

	def __init__(self):
    		HTMLParser.__init__(self)
    		self.recording = 0 
    		self.data = []

  	def handle_starttag(self, tag, attrs):
    		if tag == 'a':
          		self.recording = 1 

  	def handle_endtag(self, tag):
    		if tag == 'a':
      			self.recording -=1 

  	def handle_data(self, data):
    		if self.recording:
      			self.data.append(data)


def explore(url):

	parser = MyHTMLParser()
		
	response = urllib2.urlopen(url)
	parser.feed(response.read())

	for cont in parser.data:
		cont = cont.strip()
		
		if cont[len(cont)-1] == "/":
			urlnew = url + cont
			print urlnew
			explore(urlnew)
		else:
			temp = cont.split(".")
			if temp[len(temp) - 1] == "jpg":
				urlImg = url+cont
				print urlImg
				img = urllib2.urlopen(urlImg)
				f = open(cont,"wb")
				f.write(img.read())
				f.close()

def main():
	print "Start rolling..."

	baseAddress = "http://gags247.com/images/"

	explore(baseAddress)	


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "Force stop"
