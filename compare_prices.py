import requests
import json
from bs4 import BeautifulSoup

# Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}


def compare_prices(product_laughs, product_glomark):
    # TODO: Aquire the web pages which contain product Price
    product_laughs = requests.get(product_laughs, headers=user_agent)
    product_glomark = requests.get(product_glomark, headers=user_agent)


    # TODO: LaughsSuper supermarket website provides the price in a span text.
    soup_laughs = BeautifulSoup(product_laughs.text, 'html.parser')
    price_laughs = soup_laughs.find_all('span', {'class': 'price'})[1].text
    product_name_laughs = soup_laughs.find_all('h1')[0].text

    # TODO: Glomark supermarket website provides the data in jason format in an inline script.
    # You can use the json module to extract only the price

    soup_glomark = BeautifulSoup(product_glomark.text, 'html.parser')
    script_glomark = soup_glomark.find('script', {'type': 'application/ld+json'}).text
    data_glomark = json.loads(script_glomark)
    price_glomark = data_glomark['offers'][0]['price']
    product_name_glomark =data_glomark['name']


    # TODO: Parse the values as floats, and print them.
    price_laughs = price_laughs.replace("Rs.", "")
    price_laughs = float(price_laughs)
    price_glomark = float(price_glomark)

    print('Laughs  ', product_name_laughs, 'Rs.: ', price_laughs)
    print('Glomark ', product_name_glomark, 'Rs.: ', price_glomark)

    if (price_laughs > price_glomark):
        print('Glomark is cheaper Rs.:', price_laughs - price_glomark)
    elif (price_laughs < price_glomark):
        print('Laughs is cheaper Rs.:', price_glomark - price_laughs)
    else:
        print('Price is the same')