from bs4 import BeautifulSoup as bs
import requests
import os


def generate_meme(_id, *args):
    URL = 'https://api.imgflip.com/caption_image'
    params = {
        'username': os.environ.get("USERNAME"),
        'password': os.environ.get("PASSWORD"),
        'template_id': _id,
        'text0': None,
        'text1': None,
    }
    for i in range(0, len(args)):
        params['text' + str(i)] = args[i]
    print(params)
    response = requests.request('POST', URL, params=params).json()
    print(response)
    data = response['data']
    return data['url']


def search_meme(name):
    memeSearch = 'https://imgflip.com/memesearch?q='
    x = name.split()
    for i in range(len(x)):
        if i == 0:
            memeSearch = memeSearch + x[i]
        else:
            memeSearch = memeSearch + '+' + x[i]

    page = requests.get(memeSearch)
    soup = bs(page.content, 'html5lib')
    s = soup.findAll('a')
    links = []

    for i in s:
        links.append(i['href'])

    ids = []

    for i in links:
        x = i.split('/')
        for k in range(0, len(x)):
            if x[k] == "memetemplate":
                ids.append(x[k + 1])

    print(ids)
    return ids[0]


def get_meme(name, *args):
    id_ = search_meme(name)
    link = generate_meme(id_, *args)
    return link
