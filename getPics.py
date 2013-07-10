#!/usr/bin/python

import sys
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
        if cont[-1] == "/":
            urlnew = url + cont
            sys.stdout.write("[Dir Found] %s\n" % urlnew)
            explore(urlnew)
        else:
            if cont.split(".")[-1] == "jpg":
                urlImg = url + cont
                sys.stdout.write("[Downloading Image] %s\r" % urlImg)
                img = urllib2.urlopen(urlImg)
                f = open(cont,"wb")
                f.write(img.read())
                f.close()
                sys.stdout.write("[Downloaded] %s\n" % urlImg)

def main():
    print "Start rolling..."

    baseAddress = "http://gags247.com/images/"

    explore(baseAddress)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print "Force stop"
