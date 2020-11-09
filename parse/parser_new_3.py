# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
from time import sleep
import socket
import socks

from random import choice
from urllib.parse import urlencode
from urllib.request import urlopen
from random import uniform
import urllib.parse


def get_html(url, useragent, proxy):
    r = requests.get(url=url, headers=useragent, proxies = proxy, timeout=20)
    return r.text


def get_info_1(html, list_of_data):
    full_list = list_of_data
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.find_all('table', {'class': 'w3-table w3-bordered w3-striped'})
    head = soup.find('h1')
    if tables[0].contents[1].text == '':
        full_list.append('empty_string')
        return full_list
    else:
        for item in tables:
            try:
                for m in item.contents:
                    if m.contents[0].text == 'ФИО':
                        pass
                    else:
                        city = head.text
                        list_of_data = m.contents
                        new_list_of_data = []
                        for i in list_of_data:
                            new_list_of_data.append(i.text)
                        new_list_of_data.insert(0, city)
                        final_data = ';'.join(new_list_of_data)
                        full_list.append(final_data)
            except Exception as exc:
                print(exc)
        # print(html)
        print(len(full_list))
        return full_list


def write_to_file(list_of_data):
    for item in list_of_data:
        fe = open('base_test.txt', 'a', encoding='utf8')
        fe.write('{}\n'.format(item))
        fe.close()


def checkIP():
    ip = requests.get('http://checkip.dyndns.org').content
    soup = BeautifulSoup(ip, 'html.parser')
    return (soup.find('body').text)


def main():
    # socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
    # socket.socket = socks.socksocket

    proxies = open('proxy.txt').read().split('\n')
    useragents = open('useragents.txt').read().split('\n')
    fucking_ip = []
    with open('links_total.txt', 'r', encoding='utf8') as ff:
        for line in ff:
            url = line[:-1]
            # url2 = url.replace('http://', '')
            # url2 = urllib.parse.quote(url2.encode('utf-8'))
            # url2 = 'http://' + url2
            list_of_data = []

            # counter = 0
            for i in range(60):
                while not list_of_data:
                    useragent = {'User-Agent': choice(useragents)}
                    proxy = {'http':(proxies)}
                    try:
                        print(url)
                        print(fucking_ip)
                        ololo_ip = checkIP()
                        print(ololo_ip)
                        if ololo_ip in fucking_ip:
                            print('жду смену айпи')
                            sleep(9)
                        else:
                            pass
                        html = get_html(url=url, useragent=useragent, proxy = proxy)
                        list_of_data = get_info_1(html, list_of_data=list_of_data)
                        if len(list_of_data) == 0:
                            if ololo_ip in fucking_ip:
                                pass
                            else:
                                fucking_ip.append(ololo_ip)
                    except Exception as ff:
                        print(ff)

                else:
                    break
            write_to_file(list_of_data)


if __name__ == '__main__':
    main()
