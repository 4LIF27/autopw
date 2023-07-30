#tinggal pake apa susahnya
B='https://www.facebook.com'
H=input
A=print
import requests as C,re,os,sys,re,datetime
from time import time as G,sleep
from bs4 import BeautifulSoup as J
from urllib import request
E=C.Session()
D={'Host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','origin':B,'referer':B,'sec-ch-ua':'";Not A Brand";v="99", "Chromium";v="94"','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'}
E.headers.update(D)
def K():B='                         \n _____ _____ _____ _____ \n|__   |  |  |  |  |  |  |\n|   __|t.me/axv_id|  | -|\n|_____|__|__|_____|__|__|\n Password auto changer\n';A(B)
def F():
	D='|';K()
	try:A(' masukan format uid|pw|cokie');L=H(' masukan file : ');B=H(' masukan new pw : ');id=open(L,'r').read().splitlines();A(f" total akun : {len(id)}")
	except FileNotFoundError:A('file tidak ada')
	for F in id:
		G=F.split(D)[0];I=F.split(D)[1];M=F.split(D)[2];J={'cookie':M};C=E.get('https://mbasic.facebook.com/settings/security/password/?',cookies=J).text;next=re.findall('action\\="(.*?)"',C)[1];N={'fb_dtsg':re.findall('name="fb_dtsg" value="(.*?)"',C),'jazoest':re.findall('name="jazoest" value="(.*?)"',C),'password_change_session_identifier':re.findall('name="password_change_session_identifier" value="(.*?)"',C),'password_old':I,'password_new':B,'password_confirm':B,'save':'Simpan perubahan'};O=E.post('https://mbasic.facebook.com'+str(next),cookies=J,data=N).text
		if'Kata Sandi Telah Diubah'in O:A(f" done {G} {B}");open(' new.txt','a').write(G+D+B+'\n')
		else:A(f" failed {G} {I}")
	exit('\n done,program telah selesai')
F()
