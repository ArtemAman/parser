# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import socket
import socks
from random import choice
from urllib.parse import urlencode
from urllib.request import urlopen
import urllib.parse

def get_html(url):
    r = requests.get(url, timeout=15)
    return r.text


def get_info_1(html, list_of_links):
    full_list = list_of_links
    soup = BeautifulSoup(html, 'lxml')
    for link in soup.find_all('a'):
        a = link.get('href')
        b = a[-4:]
        if b != 'html':
            pass
        else:
            full_list.append(a)
    print(full_list)
    return full_list


def write_to_file(list_of_links):
    for i in list_of_links:
        fe = open('full_links.txt', 'a', encoding='utf8')
        fe.write('{}{}\n'.format('http://nomer-org.website', i))
        fe.close()


def main():
    socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
    socket.socket = socks.socksocket

    with open('cities_links.txt', 'r', encoding='utf8') as ff:
        for line in ff:
            url = line[:-1]
            list_of_links = []
            for i in range(50):
                if not list_of_links:
                    try:
                        html = get_html(url=url)
                        list_of_links = get_info_1(html, list_of_links=list_of_links)
                    except:
                        print(f'дд')

                else:
                    break
            write_to_file(list_of_links)




if __name__ == '__main__':
    main()
