import os, sys, time, random, uuid, string
from concurrent.futures import ThreadPoolExecutor as tred

# --- Modules Check ---
try:
    import requests
    from rich.panel import Panel
    from rich import print as rprint
except ImportError:
    os.system('pip install requests rich')
    import requests
    from rich.panel import Panel
    from rich import print as rprint

# --- Admin Details ---
DEVELOPER = "ATTA PATHAN" 
CHANNEL_LINK = "https://whatsapp.com/channel/0029VbBbJoMD38CXtkQTqB0c"
VERSION = "1.0"

# --- Colors ---
W = "\033[1;37m"
G = "\033[1;32m"
R = "\033[1;31m"
B = "\033[1;34m"
Y = "\033[1;33m"

# --- Advanced UA Generator (High Success Rate) ---
def get_user_agent():
    android_version = random.randint(10, 13)
    fb_version = f"{random.randint(300, 400)}.0.0.{random.randint(10, 99)}"
    fb_build = random.randint(300000000, 400000000)
    # Redmi Note 8 Pro specific UA for bypassing checkpoints
    ua = (f"Mozilla/5.0 (Linux; Android {android_version}; Build/QP1A.{random.randint(111111, 999999)}.020; wv) "
          f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randint(90, 120)}.0.0.0 Mobile Safari/537.36 "
          f"[FBAN/FB4A;FBAV/{fb_version};FBPN/com.facebook.katana;FBLC/en_US;FBBV/{fb_build};"
          f"FBCR/Jazz;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 8 Pro;]")
    return ua

# --- Banner ---
def banner():
    os.system('clear')
    # Atta Pathan Brand Banner
    rprint(Panel(f"""[bold red]
 █████╗ ████████╗████████╗ █████╗ 
██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗
███████║   ██║      ██║   ███████║
██╔══██║   ██║      ██║   ██╔══██║
██║  ██║   ██║      ██║   ██║  ██║
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝
[bold white]   ██████╗  █████╗ ████████╗██╗  ██╗ █████╗ ███╗   ██╗
   ██╔══██╗██╔══██╗╚══██╔══╝██║  ██║██╔══██╗████╗  ██║
   ██████╔╝███████║   ██║   ███████║███████║██╔██╗ ██║
   ██╔═══╝ ██╔══██║   ██║   ██╔══██║██╔══██║██║╚██╗██║
   ██║     ██║  ██║   ██║   ██║  ██║██║  ██║██║ ╚████║
   ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝""", 
    title="[bold yellow]⚡ ATTA PATHAN TOOL ⚡[/bold yellow]", border_style="red"))
    
    rprint(Panel(f"""[bold green]DEVELOPER  : [bold white]{DEVELOPER}
[bold green]VERSION    : [bold white]{VERSION}
[bold green]CHANNEL    : [bold cyan]ILLEGAL HACKER
[bold green]STATUS     : [bold yellow]FREE TOOL""", border_style="green"))
    
    print(f"{Y} FOLLOW CHANNEL: {W}{CHANNEL_LINK}")
    print(f"{B}————————————————————————————————————————————————")

# --- Stats ---
loop = 0
oks = []
cps = []

# --- Crack Logic (Template) ---
def crack_logic(uid, pwx, tl):
    global loop, oks, cps
    sys.stdout.write(f'\r{W}[{B}ATTA-PATHAN{W}] {G}{loop}{W}/{R}{tl} {G}OK:{len(oks)} {Y}CP:{len(cps)}'); sys.stdout.flush()
    
    # Yahan requests ka code aayega jo pehle scripts mein tha
    # example: requests.post('https://b-graph.facebook.com/auth/login', ...)
    
    loop += 1

# --- Start Cloning ---
def start_cloning(prefix, type_name):
    banner()
    try:
        limit = int(input(f" {W}[{G}?{W}] {G}ENTER LIMIT (e.g 10000): {W}"))
    except: limit = 5000
    
    ids = []
    for _ in range(limit):
        if prefix == "100000": # 2009-2010
            num = ''.join(random.choice(string.digits) for _ in range(9))
        else: # 2011-2014
            num = ''.join(random.choice(string.digits) for _ in range(10))
        ids.append(prefix + num)
    
    banner()
    print(f" {W}[{G}●{W}] {G}TOTAL IDS  : {W}{len(ids)}")
    print(f" {W}[{G}●{W}] {G}TYPE       : {W}{type_name}")
    print(f" {W}[{G}●{W}] {R}USE AIRPLANE MODE EVERY 5 MIN")
    print(f"{B}————————————————————————————————————————————————")
    
    with tred(max_workers=30) as execute:
        for uid in ids:
            # Common password list
            pwx = [uid[6:], uid, '123456', '1234567', '12345678', '572737', '575757']
            execute.submit(crack_logic, uid, pwx, len(ids))

# --- Main Menu ---
def menu():
    banner()
    print(f" {W}[{R}01{W}] {G}OLD CLONING (2009-2010)")
    print(f" {W}[{R}02{W}] {G}OLD CLONING (2011-2014)")
    print(f" {W}[{R}03{W}] {G}JOIN WHATSAPP CHANNEL")
    print(f" {W}[{R}00{W}] {G}EXIT TOOL")
    
    choice = input(f"\n {B}SELECT : {G}")
    
    if choice in ['1', '01']:
        start_cloning("100000", "2009-2010")
    elif choice in ['2', '02']:
        start_cloning("10000", "2011-2014")
    elif choice in ['3', '03']:
        os.system(f'xdg-open {CHANNEL_LINK}')
        menu()
    else:
        sys.exit()

if __name__ == "__main__":
    menu()
