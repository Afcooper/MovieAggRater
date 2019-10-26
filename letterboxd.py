import requests
from bs4 import BeautifulSoup, NavigableString
import Urls
import requests
from bs4 import BeautifulSoup
import lxml
import json
import Urls
import re

tags = ['ul', 'img', 'a', 'span', 'p']
class letterboxd:
    def __init__(self, url):
        #initialize url as a variable and automatically perform these functions
        self.url = url
        self.getInfo()

    titles = []
    paragraphs = []
    hrefs = []

    dict = []

    def getInfo(self):
        result = requests.get(self.url)
        content = result.content
        soup = BeautifulSoup(content)
        samples = soup.find_all("li")
        set = {}
        count = 0
        for node in samples:
        # this will go though each li element and will find the a h2 p variables and add them to a dictionary
        # this dictionary will contain the file location, the title, and paragraph of the story
        #then it will create a list of dictionaries (stories)
            temp2 = {}
            try:
                #print(child.name)
                title = node.find_all('img')[0].attrs['alt']
                img_href = node.find_all('img')[0].attrs['src']
                rating = node.find_all('p')[0].contents[0]
                temp2['title'] = title
                temp2['img'] = img_href
                temp2['ratings'] = rating
                set[title] = temp2
            except:
                continue
        self.dict = set
