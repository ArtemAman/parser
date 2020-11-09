import time
import urllib.parse

from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlencode
import requests
import socket
import socks

url = 'http://free-proxy.cz/ru/'
url2 = 'http://nomer-org.website'
list_of_good_cites = []
url_list_cities = []
proxylist = []
used_proxy_list = []


# session = requests.session()
# for i in range(10000):
#     response = session.get(url2)
#     html = response.content
#     print(html[:1000])
#     time.sleep(1)

#
def get_proxy():
    '''функция для получения списка прокси'''

    session = requests.session()
    html_doc = session.get(url)
    soup = BeautifulSoup(html_doc.content, 'lxml')
    tables = soup.find_all('td', {'class': 'left'})
    for item in tables:
        m = item.contents
        fe = open('proxy.txt', 'a', encoding='utf8')
        fe.write('{}{}:{}\n'.format('http://', m[0].text, m[1].text))
        fe.close()

    print(proxylist)


get_proxy()


# def parse_cities():
#     html_doc = requests.get(url2, proxies=proxies)
#     soup = BeautifulSoup(html_doc.content, 'lxml')
#
#     for link in soup.find_all('a'):
#         url_list_cities.append(link.get('href'))
#         fe = open('cities_links.txt', 'a', encoding='utf8')
#         fe.write('{}{}\n'.format('http://nomer-org.website', link.get('href')))
#         fe.close()










#
#
# with open('proxy.txt', 'r', encoding='utf8')as pr:
#     for line in pr:
#         a = line[:-1]
#         proxies = {"http": a, }
#         try:
#             parse_cities()
#         except requests.exceptions.ProxyError:
#             print('ololo')

# for i in url_list_cities:
#     full_url_to_parse = 'http://nomer-org.website' + i
#     session = requests.session()
#     html_doc = session.get(full_url_to_parse, proxies=proxies)
#     soup = BeautifulSoup(html_doc.content, 'lxml')
#     for link in soup.find_all('a'):
#         a = link.get('href')
#         b = a[-4:]
#         if b != 'html':
#             pass
#         else:
#             fe = open('links.txt', 'a', encoding='utf8')
#             fe.write('{}{}\n'.format('http://nomer-org.website', link.get('href')))
#             fe.close()
#             time.sleep(1)
#



# url = 'http://nomer-org.website/azov/fio_%25D0%2590_pagenumber_1.html'
#
# import sqlite3
#
# conn = sqlite3.connect('ukranians.db')
#
# conn.text_factory = bytes
#
# cursor = conn.cursor()
#
#
# #
# socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
# socket.socket = socks.socksocket


# with open('full_links.txt', 'r', encoding='utf8') as ff:
#     for line in ff:
#         url = line[:-1]
#         r = requests.get(url)
#         soup = BeautifulSoup(r.text, 'html.parser')
#         tables = soup.find_all('table', {'class': 'w3-table w3-bordered w3-striped'})
#         head = soup.find('h1')
#         try:
#             for item in tables:
#                 for m in item.contents:
#                     if m.contents[0].text == 'ФИО':
#                         pass
#                     else:
#                         city = head.text
#                         FIO = m.contents[0].text
#                         tel = m.contents[1].text
#                         street = m.contents[2].text
#                         house = m.contents[3].text
#                         corp = m.contents[4].text
#                         flat = m.contents[5].text
#                         fe = open('base.txt', 'a', encoding='utf8')
#                         fe.write('{};{};{};{};{};{};{}\n'.format(city, FIO, tel, street, house, corp,flat))
#                         fe.close()
#         except:
#             print(f'smth wrong')
#             continue




