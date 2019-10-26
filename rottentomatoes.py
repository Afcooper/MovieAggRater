import requests
from bs4 import BeautifulSoup, NavigableString
import Urls
import requests
from bs4 import BeautifulSoup
import lxml
import json
import Urls
import re

tags = ['tr', 'a', 'td', 'title']
class rottentomatoes:
    def __init__(self, url):
        #initialize url as a variable and automatically perform these functions
        self.url = url
        self.getInfo()
        #self.deleteEmpty()

    titles = []
    paragraphs = []
    hrefs = []

    #self.dict
    #this is the dictionary of the class and should only have movies specific to it
    dict = []

    def getInfo(self):
        result = requests.get(self.url)
        content = result.content
        soup = BeautifulSoup(content)
        samples = soup.find_all("tr")
        set = {}
        count = 1
        for node in samples:
        # this will go though each li element and will find the a h2 p variables and add them to a dictionary
        # this dictionary will contain the file location, the title, and paragraph of the story
        #then it will create a list of dictionaries (stories)
            temp2 = {}
            # if title != []:
            #     for col in title:
            #         if col.string == 'titleColumn':
            #             title = col
            #     title = title.find('a')
            test = ''

            #this part gathers all of the information on the movies
            #if there is no info or wrong info it will continue on and discard useless info
            try:
                totals = stripText(node.text)

                rank = int(totals.pop(0))
                rating = int(totals.pop(0))
                num_of_reviews = int(totals.pop(-1))

                title = ''
                for str in totals:
                    title+= str
                #checks to make sure this is a valid list that we can add to the data if not it will not add these variables to the data set
                assert rank is not None
                assert rating is not None
                assert num_of_reviews is not None
                assert title is not ''
                assert title is not None

                temp2['title'] = title
                temp2['critic_reviews'] = num_of_reviews
                temp2['ratings'] = rating
                temp2['rank'] = rank

                set[title] = temp2
            except:
                continue


        self.dict = set



def stripText(text):
    #get rid of all the crap in the text
    text = text.replace('\n', ' ').strip()
    text = text.replace('.', ' ')
    text = text.replace('%', '')
    list = text.split(' ')
    result = []

    #add only words to the list
    for i in list:
        if i != '':
            result.append(i)
    return result