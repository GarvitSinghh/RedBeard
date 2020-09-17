import requests
import json
import random
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import os


def search_gif(search_item, limit):
    apikey = os.environ.get("API_KEY")
    r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_item, apikey, limit))

    if r.status_code == 200:
        loaded = json.loads(r.content)
        gif = random.choice(loaded['results'])
    else:
        gif = None
    return gif.get('url', None)


def check(author):
    def inner_check(message):
        return message.author == author

    return inner_check


def getAnswer(question, myDriver):
    box = myDriver.find_element_by_xpath("//input[@name='stimulus']")
    box.send_keys(question + Keys.ENTER)
    time.sleep(5.5)
    answer = myDriver.find_element_by_xpath("//*[@id=\"line1\"]/span[1]").text
    return answer


def get_gif_link(link):
    page = requests.get(link)
    soup = bs(page.content, "html.parser")
    gif = soup.findAll('img')[2]
    return gif['src']
