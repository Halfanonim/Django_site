from django.shortcuts import render
import requests
import json
from bs4 import BeautifulSoup
from django.http import HttpResponse
l=''
s=0
url=requests.get("https://api.coinbase.com/v2/exchange-rates?currency=USDT")
data=url.json()
Final=data["data"]["rates"]["RUB"]
# print(Final)


url1=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=tron&vs_currencies=usd&include_last_updated_at=true")
data1=url1.json()
Final1=data1['tron']['usd']
# print(Final1)
# url3=requests.get("https://weather.rambler.ru/v-moskve/today/")
# soup = BeautifulSoup(url3.text, "html.parser")
# pres=soup.findAll('span', class_='VaOz d2qU')
r=len('<span class="VaOz d2qU">Давление ')
# f=pres[1]
# f1=str(pres[0])
l1=len('<span class="VaOz d2qU">')
l2=len("</span>")
# l3=len(f1)
# print(f1[l1:l3-l2])
# print(r)
# print(str(f)[r:r+3])
# print(l)
# print(pres)
url4=requests.get("https://ru-meteo.ru/moscow/hour")
soup1 = BeautifulSoup(url4.text, "html.parser")
# print(soup1)
temp=soup1.findAll('div', class_='current-temp')
condit=soup1.findAll('div',class_='conditions')
#wind=soup1.findAll('li', title='Ветер в румбах горизонта  (откуда дует)')
#pressure=soup1.findAll('li', title='Атмосферное давление на уровне станции 996.4 гПа')
temp1=str(temp)
temp2=BeautifulSoup(temp1,"html.parser")
# print(temp2)
temp3=temp2.findAll(string=True)
# print(temp3)
temp4=str(temp3[1])
# print(str(temp3[1]))
# print(temp)
condit1=str(condit)
condit2=BeautifulSoup(condit1,"html.parser")
condit3=condit2.findAll(string=True)
# print(condit3)
wind1=str(condit3[3])
# print(wind1)
pressure1=str(condit3[6])
# print(pressure1)
# print(condit)
# print(wind)
# print(pressure)
# pres=soup.findAll('span', class_='VaOz d2qU')

def index(request):
    return HttpResponse(f"""
           <p>Курс 1: {Final}</p>
           <p>Курс 2: {Final1}</p>
           <p>Температура: {temp4}</p>
       """)
