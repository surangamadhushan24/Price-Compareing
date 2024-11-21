from bs4 import BeautifulSoup
import requests
import lxml
import re

urlcargils = 'https://cargillsonline.com/Web/ProductDetails?ID=1txN9bCQaJL+kazjX7SJTw=='
urlKeels = 'https://glomark.lk/top-crust-bread/p/13676'

result1 = requests.get(urlcargils).text
doc = BeautifulSoup(result1, 'html.parser')

result2 = requests.get(urlKeels).text
doc1 = BeautifulSoup(result2, 'html.parser')

getHtags = doc.find('h4', class_='txtSmall')
getprice = getHtags.text.split()
price = getprice[0:2]

print(str(price[0] +price[1]))

getTags = doc1.find_all('div', class_='price')
price_keels = getTags
print(price_keels)



