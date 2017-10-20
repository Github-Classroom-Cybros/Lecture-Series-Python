from urlparse import urlparse
from bs4 import BeautifulSoup
import requests
import io
import json
import praw

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


def scrape_reddit(url):
    reddit = praw.Reddit(user_agent='Comment Extraction (by /u/USERNAME)',
                         client_id='INSERT CLIENT ID', client_secret="INSERT CLIENT SECRET")
    submission = reddit.submission(url=URL2)
    output = dict()
    output['Submission'] = submission.title
    output['Comments'] = list()
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        ans = dict()
        try:
            ans['Author'] = top_level_comment.author.name
        except:
            ans['Author'] = "Hidden"
        ans['content'] = top_level_comment.body
        output['Comments'].append(ans)
    json_object = json.dumps(output, ensure_ascii=False, indent=4)
    io.open('reddit_output.json', 'w').write(json_object)

scrape_reddit('https://www.reddit.com/r/AskReddit/comments/4lx5a9/serious_what_is_the_creepiest_most_blood_chilling/')
