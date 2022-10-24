from bs4 import BeautifulSoup
import requests

class PrintDollar:

    def __init__(self):
        self.link = 'https://cbr.ru/'
        self.src = requests.get(self.link).text
        self.soup = BeautifulSoup(self.src, 'lxml')
        self.cur_currency_name = self.soup.find('div', class_='col-md-2 col-xs-9 _dollar')
        self.cur_currency_val_list = self.soup.find_all('div', class_='col-md-2 col-xs-9 _right mono-num')
        self.cur_currency_val = self.cur_currency_val_list[1]

    def __str__(self) -> str:
        return '{0} : {1}'.format(self.cur_currency_name.text, self.cur_currency_val.text.strip())
