from bs4 import BeautifulSoup
import requests

class CurrencyParsing:
# доллар - USD
# евро - EUR
# юань - СNY
# фунт стерлингов - GBP

    def __init__(self, cur_name):
        self.__soup = BeautifulSoup(requests.get('https://www.banki.ru/products/currency/cb/').text, 'lxml')
        self.__cur_name = cur_name

    def get_val(self):
        return self.__soup.find('tr', {'data-test': 'currency-table-row', 'data-currency-code': self.__cur_name}).find_all('td')[3].text