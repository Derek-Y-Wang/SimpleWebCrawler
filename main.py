import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Facebook'


class WikiGatherer:

    def __init__(self, url):
        self.url = url
        self.links = set()
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
            self.links.add(href)
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


class PERatio:

    def __init__(self, stock_code):
        self.stock_code = stock_code
        self.source = "https://ca.finance.yahoo.com/quote/" + \
                      stock_code.upper() + "?p=" + stock_code.upper()

    def stock_code_verification(self):
        """
        Checks if the stock code is legit
        :return:
        """
        source_code = requests.get(self.source)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="lxml")
        for code in soup.findAll('span', {
            'class': 'D(b) Ta(c) W(100%) Fz(m) C($c-fuji-grey-j) Mb(10px) Fw(500) Ell'}):
            if 'No results for' in code.string:
                return False
        return True

    def finance_crawler(self):
        if not self.stock_code_verification():
            return "No result for " + self.stock_code
        p = " "
        e = " "
        source_code = requests.get(self.source)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="lxml")

        for string in soup.findAll('span', {'class':
                                                'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'}):
            p = string.string.replace(",", '')
            print("p=" + p)

        e = soup.findAll('span', {'class': 'Trsdu(0.3s)'})[12].string.replace(
            ",", '')
        print("e=" + e)

        ratio = float(p) / float(e)
        if ratio < 0:
            return 0
        return ratio


class AmazonCrawler:
    def __init__(self, url):
        self.url = url

    def simple_crawl(self):
        source_code = requests.get(self.url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="lxml")
        for link in soup.findAll('a'):
            href = link.string
            print(href)

a = PERatio('TLSA')
print(a.stock_code_verification())
print(a.finance_crawler())

b = AmazonCrawler('https://www.amazon.ca/s?k=gaming+mouse&ref=nb_sb_noss_2')
b.simple_crawl()
