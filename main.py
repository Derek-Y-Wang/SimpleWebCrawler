import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Facebook'


def lenovo_crawler(max_pages):
    page = 1
    while page <= max_pages:

        source_code = requests.get(URL)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="lxml")
        count = 0
        for link in soup.findAll('a', {'class': 'external text'}):
            href = link.get('href')
            print(str(count) + href + '\n')
            count += 1
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="lxml")
    for item_price in soup.findAll('a', {'class': "price-current"}):
        print(item_price)


lenovo_crawler(2)
