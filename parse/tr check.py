# -*- coding: utf-8 -*-

import socket

import requests
from bs4 import BeautifulSoup
from time import sleep
import socket


from random import choice
from urllib.parse import urlencode
from urllib.request import urlopen
from random import uniform
import urllib.parse

# def checkIP():
#     ip = requests.get('http://checkip.dyndns.org').content
#     soup = BeautifulSoup(ip, 'html.parser')
#     print(soup.find('body').text)
#
#
# socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
# socket.socket = socks.socksocket
# checkIP()

#
# ''' для разделения базы на много файлов'''
#
# #
# def split_list(alist, wanted_parts):
#     length = len(alist)
#     return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
#             for i in range(wanted_parts)]
#
#
# with open('base_2/links_total.txt', 'r', encoding='utf-8') as file:
#     ololo = file.read().split('\n')
#     a = (split_list(ololo, wanted_parts=250))
#
# counter = 0
# for item in a:
#     counter += 1
#     out_file = f'base_2/links_total_{counter}.txt'
#
#     for item_2 in item:
#         with open(out_file, 'a', encoding='utf-8') as file:
#             file.write('{}\n'.format(item_2))


'''для обработк прокси'''
with open('proxy.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('proxy.txt', 'w') as fout:
    for i in data:
        fout.write(f'http://{i}')


# full_link_list = []
# ''' Для сборки в одну базу'''
# cccccounter = 0
# for i in range(150):
#     cccccounter += 1
#     with open(f'links_total_{cccccounter}.txt', 'r', encoding='utf8') as file:
#         try:
#             ololo = file.read().split('\n')
#             full_link_list.extend(ololo)
#         except:
#             print(file)
#
# for item in full_link_list:
#     fe = open('links_total_full.txt', 'a', encoding='utf8')
#     fe.write('{}\n'.format(item))
#     fe.close()





# '''Для удаления пробелов'''
# full_link_list = []
#
# with open('links_total_full.txt', 'r', encoding='utf-8') as file:
#     ololo = file.read().split('\n')
#
# for i in ololo:
#     if i == '':
#         ololo.remove(i)
#
# for item_2 in ololo:
#     with open('links_total.txt', 'a', encoding='utf-8') as file:
#         file.write('{}\n'.format(item_2))
