import requests
import re
import os
import sys
import datetime
import inquirer
from time import time as tod
from time import sleep
from bs4 import BeautifulSoup as par
from urllib import request
from platform import platform
from urllib.error import URLError
from rich import print as prints
from rich.panel import Panel
from rich.console import Console
from pprint import pprint

ses = requests.Session()

headers = {
    "Host": "mbasic.facebook.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "origin": "https://www.facebook.com",
    "referer": "https://www.facebook.com",
    "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="94"',
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"
}

ses.headers.update(headers)


def logo():
    lo = """                         
 _____ _____ _____ _____ 
|__   |  |  |  |  |  |  |
|   __|t.me/zhx_xv|  | -|
|_____|__|__|_____|__|__|
   Password auto changer
"""
    Console().print(Panel(f"{lo}", subtitle=f"[ Github.com/axv-id ]", title_align='top', width=38, padding=(0, 4)))


def menu():
    logo()
    Console().print(Panel(f"masukan pilihan", width=38, padding=(0, 4)))

    questions = [
        inquirer.List(
            "menu",
            choices=["manual", "otomatis", "exit"],
            message="pilih menu ",
        ),
    ]
    answers = inquirer.prompt(questions)
    if answers['menu'] == 'manual':
        siji()
    elif answers['menu'] == 'otomatis':
        auto()


def siji():
    Console().print(Panel(f"masukan cookies dan password yang benar!!", width=38, padding=(0, 4)))
    cok = Console().input("[bold white]?? coki : ")
    pw = Console().input("[bold white]?? password: ")
    Console().print(Panel(f"masukan password baru \nyang ingin kamu gunakan ", width=38, padding=(0, 4)))
    np = Console().input("[bold white]?? masukan new pw : ")
    cookies = {"cookie": cok}
    r = ses.get("https://mbasic.facebook.com/settings/security/password/?", cookies=cookies).text
    next = re.findall('action\="(.*?)"', r)[1]
    data = {
        "fb_dtsg": re.findall('name="fb_dtsg" value="(.*?)"', r),
        "jazoest": re.findall('name="jazoest" value="(.*?)"', r),
        "password_change_session_identifier": re.findall('name="password_change_session_identifier" value="(.*?)"', r),
        "password_old": pw,
        "password_new": np,
        "password_confirm": np,
        "save": "Simpan perubahan"
    }
    po = ses.post("https://mbasic.facebook.com" + str(next), cookies=cookies, data=data).text
    if 'Kata Sandi Telah Diubah' in po:
        Console().print(Panel(f" {np}", subtitle=f"[ DONE ]", title_align='top', width=38, padding=(0, 4)))
    else:
        Console().print(Panel(f" {pw}", subtitle=f"[ FAILED ]", title_align='top', width=38, padding=(0, 4)))
        
def auto():
    try:
        Console().print(Panel(f"masukan format uid|pw|cokie", width=38, padding=(0, 4)))
        file = Console().input("[bold white]?? masukan file : ")
        Console().print(Panel(f"masukan password baru \nyang ingin kamu gunakan ", width=38, padding=(0, 4)))
        np = Console().input("[bold white]?? masukan new pw : ")
        id = open(file,"r").read().splitlines()
        Console().print(Panel(f" TOTAL AKUN DI DALAM FILE ", subtitle=f"[ {len(id)} ]", title_align='top', width=38, padding=(0, 4)))
    except FileNotFoundError:
        print("file tidak ada")
    
    for x in id:
        uid = x.split("|")[0]
        pw = x.split('|')[1]
        cok = x.split('|')[2]
        cookies = {"cookie": cok}
        r = requests.get("https://mbasic.facebook.com/settings/security/password/?", cookies=cookies).text 
        next = re.findall('action\="(.*?)"',r)[1]

        data = {
            "fb_dtsg": re.findall('name="fb_dtsg" value="(.*?)"',r),
            "jazoest": re.findall('name="jazoest" value="(.*?)"',r),
            "password_change_session_identifier": re.findall('name="password_change_session_identifier" value="(.*?)"',r),
            "password_old": pw,
            "password_new": np,
            "password_confirm": np,
            "save": "Simpan perubahan"
        }

        po = requests.post("https://mbasic.facebook.com"+str(next), cookies=cookies, data=data).text 

        if 'Kata Sandi Telah Diubah' in po:
            Console().print(Panel(f"{uid} | {np}", subtitle=f"[ DONE ]", title_align='top', width=38, padding=(0, 4)))
            open(" new.txt","a").write(uid+'|'+np+'\n')
        else:
            Console().print(Panel(f"{uid} | {pw}",subtitle=f"[ FAILED ]",title_align='top',width=38,padding=(0,4)))
    
    Console().print(Panel(f"hasil di simpan di new.txt", subtitle=f"[ DONE ]", title_align='top', width=38, padding=(0, 4)))
    
    
menu()
