# -*- coding: utf-8 -*-

import threading
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


def get_html(url, useragent):
    r = requests.get(url=url, headers=useragent, timeout=5)
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
            except:
                print('wow')

        # print(html)
        print(len(full_list))
        return full_list


def del_from_file(file_to_change):
    with open(file_to_change, 'r', encoding='utf8') as fin:
        data = fin.read().splitlines(True)
    with open(file_to_change, 'w', encoding='utf8') as fout:
        fout.writelines(data[1:])



def write_to_file(list_of_data, output_file):
    for item in list_of_data:
        fe = open(output_file, 'a', encoding='utf8')
        fe.write('{}\n'.format(item))
        fe.close()


def checkIP():
    ip = requests.get('http://checkip.dyndns.org').content
    soup = BeautifulSoup(ip, 'html.parser')
    return (soup.find('body').text)


def main(input_file, output_file):
    socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
    socket.socket = socks.socksocket

    useragents = open('useragents.txt').read().split('\n')

    with open(input_file, 'r', encoding='utf8') as ff:
        for line in ff:
            url = line[:-1]
            list_of_data = []
            for i in range(300):
                while not list_of_data:
                    useragent = {'User-Agent': choice(useragents)}
                    try:
                        sleep(uniform(1, 3))
                        html = get_html(url=url, useragent=useragent)
                        list_of_data = get_info_1(html, list_of_data=list_of_data)
                    except Exception as ff:
                        print(ff)

                else:
                    break
            write_to_file(list_of_data, output_file)
            del_from_file(input_file)


# if __name__ == '__main__':
#     main()

cccccounter = 0
for i in range(150):
    cccccounter += 1
    t = threading.Thread(target=main, args=(f'links_total_{cccccounter}.txt', f'base_{cccccounter}.txt'))
    t.start()
