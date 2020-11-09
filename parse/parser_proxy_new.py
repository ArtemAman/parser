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

url = 'https://hidemy.name/ru/proxy-list/?type=hs#list/'
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

socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket

# def get_proxy():
#     '''функция для получения списка прокси'''
#
#     session = requests.session()
#     html_doc = session.get(url)
#     soup = BeautifulSoup(html_doc.content, 'lxml')
#     tables = soup.find_all('tr')
#     for item in tables:
#         m = item.contents
#         fe = open('proxy.txt', 'a', encoding='utf8')
#         fe.write('{}{}:{}\n'.format('http://', m[0].text, m[1].text))
#         fe.close()
#
#     print(proxylist)


# get_proxy()


socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket


def get_proxy_2():
    '''функция для получения списка прокси'''

    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.content, 'lxml')
    tables = soup.find_all('tr')
    for item in tables:
        m = item.contents
        fe = open('proxy.txt', 'a', encoding='utf8')
        fe.write('{}{}:{}\n'.format('http://', m[0].text, m[1].text))
        fe.close()

    print(proxylist)


get_proxy_2()
