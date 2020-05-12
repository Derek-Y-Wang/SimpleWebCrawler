import requests
from bs4 import BeautifulSoup

URL = "https://www.lenovo.com/us/en/outletus/laptops/c/LAPTOPS?q=%3Aprice-asc%3AfacetSys-Condition%3ANew%3AfacetSys-Condition%3ARefurbished%3AfacetSys-Memory%3A16+GB%3AfacetSys-Memory%3A8+GB%3AfacetSys-HardDrive%3A1+TB%3AfacetSys-HardDrive%3A512+GB+Solid+State%3AfacetSys-Processor%3AIntel%C2%AE+Core%E2%84%A2+i7&uq=&text=#"


def lenovo_crawler(url):

    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features='lxml')
    print("souped")
    for link in soup.findAll('a', {"class": "facetedResults-title"}):
        print('run')
        href = "lenovo.com" + link.get('href')
        # get_single_item_data(href)
        print(href)
        print('========================================')


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="lxml")
    for item_price in soup.findAll('a', {'class': "price-current"}):
        print(item_price)


lenovo_crawler(URL)

