from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

n_html = requests.get('https://khabarpu.com/pu/varzesh-pu/latest-sports-news.htm')
n_soup = BeautifulSoup(n_html.content, 'html.parser')
n_heading = n_soup.find('div', {'id': 'news_div'}).find_all('a', title=True)
n_links = n_soup.find('div', {'id': 'news_div'}).find_all('a')

n_news = []
for n_header in n_heading[0:20]:
    n_news.append(n_header['title'])

n_newsli = []
for n_link in n_links[0:20]:
    n_newsli.append(n_link)


v_html = requests.get('https://www.varzesh3.com/')
v_soup = BeautifulSoup(v_html.content, 'html.parser')
v_heading = v_soup.find_all('li', {'data-filter': {'1', '3'}})

v_news = []
v_newsli = []

for v_header in v_heading[0: 20]:
    v_news.append(v_header.get_text())


m = 0
n = 20
while m < n:
    li = str(v_heading[m]).split()
    v_newsli.append(li[4])
    m += 1


def index(request):
    return render(request, 'news/index.html', {'n_news': n_news, 'n_newsli': n_newsli, 'v_news': v_news,
                                               'v_newsli': v_newsli})