# Scrapes the Quora question and its top 3 answers given a quora link

from urlparse import urlparse
from bs4 import BeautifulSoup
import requests
import io
import json

URL = 'https://www.quora.com/What-is-the-toughest-sketch-you-have-drawn'

def scrape_quora(url): 
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    output = dict()
    output['question'] = soup.find('div', {'class': 'question_text_edit'}).find('span', {'class': 'rendered_qtext'}).get_text()
    output['answers'] = list()
    for answer in soup.findAll('div', {'class': 'AnswerBase'}):
        ans = dict()
        try:
            ans['author'] = answer.find('a', {'class': 'user'}).get_text()
        except:
            ans['author'] = "Hidden"
        ans['content'] = answer.find('span', {'class': 'rendered_qtext'}).get_text()
        output['answers'].append(ans)
    json_object = json.dumps(output, ensure_ascii=False, indent=4)
    io.open('quora_output.json', 'w').write(json_object)
    
def main(url):`
    hostname = str(urlparse(str(url)).hostname.split('.')[1]).lower()
    if hostname == "quora":
        scrape_quora(url)
    else:
        print "Give a valid URL"

main(URL)
