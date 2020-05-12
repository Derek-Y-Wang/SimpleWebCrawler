import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Facebook'


class WikiGatherer:

    def __init__(self, url):
        self.url = url
        self.links = []
        self.bad = []

    def wikipedia_crawler(self):
        source_code = requests.get(self.url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="lxml")
        count = 0
        for link in soup.findAll('a', {'class': 'external text'}):
            href = link.get('href')
            if href[:2] == '//':
                href = href[2:]
            print(str(count) + ". " + href + '\n')
            self.links.append(href)
            count += 1
        # print(len(sources))

    def get_single_site_data(self):
        count = 0
        for link in self.links:
            try:
                source_code = requests.get(link)
                plain_text = source_code.text
                soup = BeautifulSoup(plain_text, features="lxml")
                print(str(count) + ". " + link)
            except:
                print(link)
            count += 1



crawl = WikiGatherer(URL)
crawl.wikipedia_crawler()
crawl.get_single_site_data()
