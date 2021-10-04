import os
os.system('cls && title Animate Status By LALOL' if os.name == 'nt' else 'clear')
import config
from config import *
import time
import colorama
from colorama import init, Fore, Back, Style
init(convert=True)
import requests
print(Fore.RED +"""
██╗░░░░░░█████╗░██╗░░░░░░█████╗░██╗░░░░░
██║░░░░░██╔══██╗██║░░░░░██╔══██╗██║░░░░░
██║░░░░░███████║██║░░░░░██║░░██║██║░░░░░
██║░░░░░██╔══██║██║░░░░░██║░░██║██║░░░░░
███████╗██║░░██║███████╗╚█████╔╝███████╗
╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░╚══════╝
""")
print(Fore.GREEN + "Animate Status By LALOL" + Fore.YELLOW)
time.sleep(3)
headers={'authorization': TOKEN}
token_check = requests.get('https://discord.com/api/v9/users/@me/library',headers=headers)
if token_check.status_code == 200 or token_check.status_code == 202:
	pass
else:
	print(Fore.RED + "Token Invalid")
	input()
	exit()
f = open('statuses.txt', encoding='utf-8')
print("Status change has begun")
def a123():
	f = open('statuses.txt', encoding='utf-8')
	for line in f:
		setting = {'custom_status': {'text': line}}
		requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=setting)
		time.sleep(delay)
	a321()
def a321():
	f = open('statuses.txt', encoding='utf-8')
	for line in f:
		setting = {'custom_status': {'text': line}}
		requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=setting)
		time.sleep(delay)
	a123()
a123()