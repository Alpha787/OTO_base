
import requests
import re
from bs4 import BeautifulSoup


url = 'https://oto-register.autoins.ru/pto/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
soup = BeautifulSoup(str(soup.find_all("tbody")[0]),'lxml')

peoples = []
status = ""
oto = ""
name = ""
adres = ""
oblast = ""

tr = soup.find_all("tr")


for t in tr:
    # print(t.find_all("td"))
    status = str(t.find_all("div")[0].get("class")[0]) + " " + str(t.find_all("div")[0].get("class")[1])

    oto = str(t.find_all("a")[1].text)
    # print(oto)
    name = str(t.find_all("b")[0].text)
    adres = str(t.find_all("a")[3].text)
    oblast = str(t.find_all("a")[4].text)

    peoples.append({
        'status': status,
        'oto': oto,
        'name': name,
        'adres': adres,
        'oblast': oblast
    })

for people in peoples:
    print("___")
    print("Статус: {} , № ОТО: {} , Краткое наименование: {} , Адрес ПТО: {} , Область аккредитации: {}".format(people["status"],people["oto"],people["name"],people["adres"],people["oblast"]))