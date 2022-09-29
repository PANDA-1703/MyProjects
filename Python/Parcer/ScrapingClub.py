import requests as rq
from bs4 import BeautifulSoup as bs 

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = rq.get(url)
soup = bs(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

for n,i in enumerate(items, start=1):
    itemName = i.find('h4', class_='card-title').text.strip()
    itemPrice = i.find('h5').text
    print(f'{n}: {itemName} за {itemPrice}')

pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')

for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        hrefval = link.get('href')
        urls.append(hrefval)

for slug in urls:
    newUrl = url.replace('?page=1', slug)
    response = rq.get(newUrl)
    soup = bs(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for n,i in enumerate(items, start=n):
        itemName = i.find('h4', class_='card-title').text.strip()
        itemPrice = i.find('h5').text
        print(f'{n}: {itemName} за {itemPrice}')