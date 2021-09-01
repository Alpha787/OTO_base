from bs4 import BeautifulSoup
# from bs4 import *
import requests
import csv
from random import choice


URL = 'https://oto-register.autoins.ru/pto/'

desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 '
                  'Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 '
                  'Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/54.0.2840.99 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) '
                  'Version/10.0.1 Safari/602.2.14',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 '
                  'Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/54.0.2840.98 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/54.0.2840.98 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 '
                  'Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/54.0.2840.99 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html')
def random_headers():
    return {'User-Agent': choice(desktop_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}


def get_html(url, params=None):
    r = requests.get(url, headers=random_headers(), params=params)
    return r

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        print(html.text)
    else:
        print('Error')

def get_content(): # получение данных из карточки
    items = soup.find_all('tbody')

    peoples = []
    for item in items:
        peoples.append({
            'status': item.find_all('div', class_='status ok '),
            'n_oto': item.find_all('a',)[0].get('href'),
            'name': item.find_all('b', class_='item-name'),

        })
        return peoples

# def get_pages_count(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     pagination = soup.find_all('a', attrs={onclick="PrimeFaces.ab({s:\"mainForm:j_idt40\",u:\"mainForm:ptoRegistryPanel\"});return false;"})
#     if pagination:
#         return int(pagination[-1].get_text())
#     else:
#         return 1

def find_pages(): # поиск по страницам
    pages = soup.find_all('a', class_='ui-commandlink ui-widget')
    return pages

def find_titles(): # поиск по загаловкам
    titles = soup.find_all('b', class_='item-name')
    titles.count(7)
    return titles

def adress_pto(): # поиск по адрессу ПТО
    pto = soup.find_all('td', 'a')
    return pto

def find_oto(): # поиск по ОТО
    oto = soup.find_all('a', 'href=#pto')
    return oto

def find_status():
    status = soup.find_all('div', class_='status ok')
    return status
print(get_content())
# print(find_titles())
# print(find_status())
# print(find_oto())
# print(find_pages())
# print(adress_pto())
# soup = BeautifulSoup(BASE_URL)
# url = BASE_URL.format()
# response = requests.get(url)
# print(url.title)
# print(dir(soup))
