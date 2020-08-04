import requests
from bs4 import BeautifulSoup

URL = 'https://www.coolblue.be/nl/product/652783/google-chromecast-v3.html'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"}


def checkprice():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('span', {"class": "js-product-name"}).get_text()
    price = soup.find('strong', {"class": "sales-price__current"}).get_text()
    converted_price = price.split(",")
    #final = float(converted_price[1])
    #price_number = float(converted_price[0] + (final/100))
    print(title)
    print("Price: " + price)


checkprice()