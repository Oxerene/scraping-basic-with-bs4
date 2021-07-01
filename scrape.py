import requests
from bs4 import BeautifulSoup
import pprint
res = requests.get('https://news.ycombinator.com')
soup = BeautifulSoup(res.text, 'html.parser')
#
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def sort_by_votes(news_li):
    return sorted(news_li, key=lambda k: k['votes'], reverse=True)


def custom_news(links, subtext):
    news_li = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href')
        vote = subtext[idx].select('.score')
        if len(vote):
            points = vote[0].getText().replace(' points', '')
            points = int(points)
            if points >= 100:
                news_li.append({'title': title, 'link': href, 'votes': points})
    return sort_by_votes(news_li)


pprint.pprint(custom_news(links, subtext))
