import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Facebook'


class WikiGatherer:

    def __init__(self, url):
        self.url = url
        self.links = set()

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
            self.links.add(href)
            count += 1
        # print(len(sources))

    def get_single_site_data(self):
        for link in self.links:
            source_code = requests.get(link)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, features="lxml")


if __name__ == '__main':
    crawl = WikiGatherer(URL)
