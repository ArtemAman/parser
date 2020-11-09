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


def get_html(url, useragent):
    r = requests.get(url=url, headers=useragent, timeout=20)
    return r.text


def get_info_1(html, list_of_links):
    full_list = list_of_links
    soup = BeautifulSoup(html, 'lxml')
    m = soup.find('center', {'class': 'siteMap'})
    for link in m.find_all('a'):
        norm_link = link.get('href')
        a = m.contents[0]
        b = ''
        for i in a:
            if i.isdigit() is True:
                b += i
            else:
                continue
        if b == '':
            break
        else:
            c = int(b) // 15
            for i in range(0, c):
                new_replace = str(i) + '.html'
                super_norm_link = norm_link.replace('1.html', new_replace)
                full_list.append(super_norm_link)
            break
    print(full_list)
    return full_list


def get_info_2(list_of_links):
    for link in list_of_links:
        url2 = ('{}{}'.format('http://nomer-org.website', link))
        # a = uniform(1, 1)
        # sleep(a)
        useragents = open('useragents.txt').read().split('\n')
        useragent = {'User-Agent': choice(useragents)}
        try:
            r = requests.get(url2, headers=useragent, timeout=20)
            soup = BeautifulSoup(r.text, 'html.parser')
            tables = soup.find_all('table', {'class': 'w3-table w3-bordered w3-striped'})
            head = soup.find('h1')
            try:
                for item in tables:
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
                            fe = open('base.txt', 'a', encoding='utf8')
                            fe.write('{}\n'.format(final_data))
                            fe.close()
            except Exception as dd:
                print(dd)
                continue
        except:
            print('ololo')


def write_to_file(list_of_links):
    for link in list_of_links:
        fe = open('links_total_norm.txt', 'a', encoding='utf8')
        fe.write('{}{}\n'.format('http://nomer-org.website', link))
        fe.close()


def checkIP():
    ip = requests.get('http://checkip.dyndns.org').content
    soup = BeautifulSoup(ip, 'html.parser')
    return (soup.find('body').text)


def main():
    socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
    socket.socket = socks.socksocket

    useragents = open('useragents.txt').read().split('\n')
    fucking_ip = []
    with open('full_links.txt', 'r', encoding='utf8') as ff:
        for line in ff:
            url = line[:-1]
            # url2 = url.replace('http://', '')
            # url2 = urllib.parse.quote(url2.encode('utf-8'))
            # url2 = 'http://' + url2
            list_of_links = []
            for i in range(60):
                if not list_of_links:
                    useragent = {'User-Agent': choice(useragents)}
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

                        # a = uniform(1, 1)
                        # sleep(a)
                        # print(a)
                        html = get_html(url=url, useragent=useragent)
                        list_of_links = get_info_1(html, list_of_links=list_of_links)
                    except Exception as dd:
                        print(dd)

                else:
                    break
                write_to_file(list_of_links)


if __name__ == '__main__':
    main()
