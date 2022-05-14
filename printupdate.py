# IT WILL PRINT THE USD PRICE IN THE TERMINAL
import requests
import json

api1 = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'


# setting the prints.json to a default value, then it will print the value
# in the first try ever
initial_value = '0'
with open('prints.json', 'w') as file:
    json.dump(initial_value, file)


def print_updates():
    response = requests.get(api1)
    price = response.json()
    price_updated = price['USDBRL']['bid']

    # open, check etc
    with open('prints.json', 'r') as file:
        test_price = json.load(file)
    if test_price != price_updated:
        test_price: str = str(price_updated)
        with open('prints.json', 'w') as file:
            json.dump(test_price, file)
        print(test_price)
    else:
        pass
