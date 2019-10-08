import requests
from bs4 import BeautifulSoup, NavigableString
import NyTimes_JSON
import requests
from bs4 import BeautifulSoup
import lxml
import json
import NyTimes_JSON
import re

tags = ['tr', 'a', 'td', 'title']
class IMDB:
    def __init__(self, url):
        #initialize url as a variable and automatically perform these functions
        self.url = url
        self.getInfo()
        #self.deleteEmpty()

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
        # this will go though each li element and will find the a h2 p variables and add them to a dictionary
        # this dictionary will contain the file location, the title, and paragraph of the story
        #then it will create a list of dictionaries (stories)
            temp2 = {}
            # if title != []:
            #     for col in title:
            #         if col.string == 'titleColumn':
            #             title = col
            #     title = title.find('a')

            try:
                rankandtitle = node.contents[3].text
                img = node.contents[1].contents[11].contents[1].attrs['src']
                numofratings = node.contents[5].contents[1].attrs['title']
                ratings = node.contents[5].contents[1].contents
                ratings = float(ratings[0])

                #Strip title and get the ranks and title name out of it
                rankandtitle = stripTitle(rankandtitle)
                rank = rankandtitle[0]
                title = rankandtitle[1]

                #call getRating
                rating, userratings = getRatings(numofratings)

                temp2['title'] = title
                temp2['rank'] = rank
                temp2['img'] = img
                temp2['userratings'] = userratings
                temp2['ratings'] = ratings

                set[title] = temp2
            except:
                continue
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



#this function will input a title. Then it will replace all the whitespace and strip the edges of the whitespace. It will then find the rank and title in the input string.
def stripTitle(title):
    title = title.replace('\n', '').strip()
    title = title.replace('.', '')
    list = title.split(' ')
    rank = 0
    result = ''
    for i in list:
        try:
            rank = int(i)
        except:
            if i != '':
                result += i + ' '
            else:
                continue

    result = re.sub("^\s+|\s+$", "", result, flags=re.UNICODE)

    return [rank, result]


#this function gets an input string that will contain the number of user ratings in it and the rating of the movie
#outputs the rating then the user ratings
def getRatings(ratings):
    ratings = ratings.replace(',', '').split(' ')
    ratinglist = []
    for i in ratings:
        try:
            ratinglist.append(float(i))
        except:
            continue

    return ratinglist[0], ratinglist[1]





if __name__ == '__main__':
    c =  IMDB(NyTimes_JSON.IMDB['movies']['top250'])
    g = IMDB(NyTimes_JSON.IMDB['tv']['top250'])
    print(g.dict)
    with open('imdbrating.json', 'w') as fp:
        json.dump(c.dict, fp,  sort_keys=True, indent=4, separators=(',',':'))
