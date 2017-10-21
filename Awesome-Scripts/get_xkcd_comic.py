#!/usr/bin/python

import sys
import requests
from bs4 import BeautifulSoup
import io
from PIL import Image


def crawler(max_pages):
    page = 1
    next_url = ''
    while page <= max_pages:
        url = 'https://xkcd.com' + next_url
        soup = BeautifulSoup(requests.get(url).text, "lxml")
        next_url = soup.findAll('a', {'rel': 'prev', 'accesskey': 'p'})[0].get('href')
        image_source = str(soup.findChild('div', {'id': 'comic'}))
        soup2 = BeautifulSoup(image_source, "lxml")
        image_url = 'https:' + soup2.findAll('img')[0].get('src')
        im = requests.get(image_url)
        image = Image.open(io.BytesIO(im.content))
        image.save(sys.argv[2]+image_url.split('/')[4])
        page += 1

crawler(int(sys.argv[1]))
