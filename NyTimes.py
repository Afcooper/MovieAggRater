import requests
from bs4 import BeautifulSoup
import NyTimes_JSON
import requests
from bs4 import BeautifulSoup
import lxml
import json
import NyTimes_JSON

tags = ['h2', 'p']
class NyTimes:
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
        samples = soup.find_all("li")
        set = {}
        count = 0
        for node in samples:
            for child in node.children:
                # this will go though each li element and will find the a h2 p variables and add them to a dictionary
                # this dictionary will contain the file location, the title, and paragraph of the story
                #then it will create a list of dictionaries (stories)
                temp2 = {}
                a = child.find('a')
                h2 = child.find('h2')
                p = child.find('p')
                if a != None:
                    try:
                        temp2['href'] = a.attrs['href']
                        self.hrefs.append(a.attrs['href'])
                    except:
                        continue

                if h2 != None:
                    try:
                        temp2['title'] = h2.string
                        self.titles.append(h2.string)
                    except:
                        continue

                if p != None:
                    try:
                        temp2['paragraph'] = p.string
                        self.paragraphs.append(p.string)
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


    def sortInfo(self):
        for i in range(0, len(self.titles)):
            self.dict[i] = [self.titles[i], self.paragraphs[i], self.hrefs[i]]

        for i in range(0,len(self.dict)):
            if self.dict[i][0] == None:
                self.dict.pop(i)
            elif self.dict[i][1] == None:
                self.dict.pop(i)
            elif self.dict[i][2] == None:
                self.dict.pop(i)

if __name__ == '__main__':
    #print(NyTimes_JSON.URLS['tech'])
    dict = {}
    count = 0
    for url in NyTimes_JSON.URLS:
        dict[url] = NyTimes(NyTimes_JSON.URLS[url])
        dict[url] = dict[url].dict
    with open('app.json', 'w') as fp:
        json.dump(dict, fp,  sort_keys=True, indent=4, separators=(',',':'))

    #print(c.titles)
    #c.sortInfo()