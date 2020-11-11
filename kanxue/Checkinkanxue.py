# -*- coding: utf8 -*-
import requests, os
from bs4 import BeautifulSoup

cookie = os.environ.get('cookie_kx')


def kxCheckin(*args):
    try:
        s = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/84.0.4147.135 Safari/537.36',
            'Cookie': cookie,
            'ContentType': 'text/html;charset=gbk'
        }

        a = s.get('https://bbs.pediy.com/user-tasks-97197-1.htm', headers=headers)
        b = BeautifulSoup(a.text, 'html.parser')
        c = b.find(attrs={"name": "csrf-token"})['content']

        if c != "":
            a = s.get('https://bbs.pediy.com/user-is_signin.htm', headers=headers)
            t = a.json()["code"]
            if t != "0":
                scurl = "https://bbs.pediy.com/user-signin.htm"
                data = {
                    "csrf_token": c
                }
                k = requests.post(scurl, data=data, headers=headers)
                print(k.json())
                code = k.json()["code"]
                if code == "0":
                    print("kanxue签到成功")
        else:
            print("csrf出错")
    except:
        print("kx出错")


if __name__ == "__main__":
    if cookie:
        kxCheckin()
