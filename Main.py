import Urls
from IMDBRating import IMDB
from letterboxd import letterboxd
from rottentomatoes import rottentomatoes
import json



if __name__ == '__main__':
    imdb_mtop250 =  IMDB(Urls.IMDB['movies']['top250'])
    imdb_tvtop250 = IMDB(Urls.IMDB['tv']['top250'])
    imdb_tvpopular250 = IMDB(Urls.IMDB['tv']['popular_top250'])
    imdb_low250 = IMDB(Urls.IMDB['movies']['low250'])
    letterbox_movies_top250_1 = letterboxd(Urls.LetterBox['movies']['top250'][0])
    letterbox_movies_top250_2 = letterboxd(Urls.LetterBox['movies']['top250'][1])
    letterbox_movies_top250_3 = letterboxd(Urls.LetterBox['movies']['top250'][2])
    letterbox_movies_top250_all = {**letterbox_movies_top250_1.dict, **letterbox_movies_top250_2.dict, **letterbox_movies_top250_3.dict}
    result = []
    rottentomatoes_top100_movies = rottentomatoes(Urls.RottenTomatoes['movies']['top100'])


    #if we want set instead of list
    #result['imdb_mtop250'] = imdb_mtop250.dict
    #result['imdb_tvtop250'] = imdb_tvtop250.dict
    #result['imdb_tvpopular250'] = imdb_tvpopular250.dict
    #result['imdb_low250'] = imdb_low250.dict
    #result['letterbox_movies_top250'] = letterbox_movies_top250_all

    #result['imdb_mtop250'] = imdb_mtop250.dict
    #result['imdb_tvtop250'] = imdb_tvtop250.dict
    #result['imdb_tvpopular250'] = imdb_tvpopular250.dict
    tomato = rottentomatoes('https://www.rottentomatoes.com/browse/tv-list-3')
    print(tomato.dict)



    result.append(imdb_mtop250.dict)
    result.append(imdb_tvtop250.dict)
    result.append(imdb_tvpopular250.dict)
    result.append(imdb_low250.dict)
    result.append(letterbox_movies_top250_all)
    result.append(rottentomatoes_top100_movies.dict)
    with open('imdbrating.json', 'w') as fp:
        json.dump(result, fp,  sort_keys=True, indent=4, separators=(',',':'))