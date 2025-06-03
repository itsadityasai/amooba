from colorama import Fore
from colorama import Style
from colorama import init

init()

def log(text):
    print(f"[+]{Fore.GREEN} {text} {Style.RESET_ALL}")

def warn(text):
    print(f"[~]{Fore.YELLOW} {text} {Style.RESET_ALL}")

def error(text):
    print(f"[-]{Fore.RED} {text} {Style.RESET_ALL}")
