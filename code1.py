# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 17:52:04 2018

@author: ACER-PC
"""
from urllib.request import urlopen
import urllib
import re
from bs4 import BeautifulSoup
import requests
import sys

counter=0
super_links=[]
#connect to a URL
def getLinks(link,word):
    try:
        global counter
        super_links.append(link)
        website = urlopen(link)
        #read html code
        html = str(website.read())
        f = open('file'+str(counter)+'.html', 'w')
        counter=counter+1
        f.write(html)
        f.close
        #counting occurrences of the word in the link
        words = re.findall(word,html)
        count=len(words)
        print('\nUrl: {}\ncontains {} occurrences of word: {}'.format(link, count, word))
        #use re.findall to get all the links        
        links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)
        for link in links:
            if link in super_links:
                continue
            else:
                getLinks(link,word)
    except urllib.error.HTTPError as err:
        return True

def main():
    url = sys.argv[1]
    word = sys.argv[2]
    getLinks(url,word)
 
if __name__ == '__main__':
    main()