import requests
from bs4 import BeautifulSoup
import NyTimes_JSON
import requests
from bs4 import BeautifulSoup
import lxml
import json
import NyTimes_JSON

tags = ['tr', 'a', 'td', 'title']
class IMDB:
    def __init__(self, url):
        #initialize url as a variable and automatically perform these functions
        self.url = url
        self.getInfo()
        self.deleteEmpty()

    titles = []
    paragraphs = []
    hrefs = []

    dict = []

    def getInfo(self):
        result = requests.get(self.url)
        content = result.content
        soup = BeautifulSoup(content)
        samples = soup.find_all("tr")
        set = {}
        count = 0
        for node in samples:
            for child in node.children:
                # this will go though each li element and will find the a h2 p variables and add them to a dictionary
                # this dictionary will contain the file location, the title, and paragraph of the story
                #then it will create a list of dictionaries (stories)
                temp2 = {}
                rating = child.find('ratingColumn imdbRating')
                title = child.find('title')
                img = child.find('img')

                if img != None:
                    try:
                        temp2['img'] = img.string
                        self.hrefs.append(img.string)
                    except:
                        continue

                if title != None:
                    try:
                        temp2['title'] = title.string
                        self.titles.append(title.string)
                    except:
                        continue

                if rating != None:
                    try:
                        temp2['rating'] = rating.string
                        self.paragraphs.append(rating.string)
                    except:
                        continue

                set[count] = temp2
                count+=1
        self.dict = set

    #deletes the empties in the dictionary that contains all the stories so it contains only valid stories
    def deleteEmpty(self):
        deleteList = []
        for i in self.dict.keys():
            if len(self.dict[i].keys()) == 0:
                deleteList.append(i)
        for x in deleteList:
            self.dict.pop(x)


if __name__ == '__main__':
    #print(NyTimes_JSON.URLS['tech'])
    dict = {}
    count = 0
    c =  IMDB(NyTimes_JSON.IMDB['movies']['top250'])
    print(c)
    print(c.dict)
    # with open('imdbrating.json', 'w') as fp:
    #     json.dump(dict, fp,  sort_keys=True, indent=4, separators=(',',':'))
