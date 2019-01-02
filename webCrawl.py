import requests
from bs4 import BeautifulSoup

##function may differ according to use case
##only works on web site with different pages
def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        #change website accordingly
        url = 'http://buckysroom.org/trade/search.php?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,features="html.parser")
        #change class accordingly
        for link in soup.findAll('a', {'class': 'd_'}):
            href = link.get('href')
            print(href)
            print("doing?")
        page += 1

#can be called with more max_pages
trade_spider(1)
