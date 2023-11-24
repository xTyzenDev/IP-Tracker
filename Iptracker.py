#!/usr/bin/python3
# IP Tracker V1.0.0
# Code By: xTyzenツ.py

import os
import sys
import json
import requests
import time
from pystyle import *
from colorama import *

os.system("cls || clear")

intro = """  ██╗██████╗    ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
  ██║██╔══██╗   ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
  ██║██████╔╝█████╗██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
  ██║██╔═══╝ ╚════╝██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
  ██║██║           ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
  ╚═╝╚═╝           ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝by xTyzenツIV                        
                              [!] Updated [!]

                             >> Press Enter <<"""

Anime.Fade(Center.Center(intro), Colors.white_to_red, Colorate.Vertical, interval=0.035, enter=True)

def aff():
  print(f"""{Fore.LIGHTRED_EX}    ________      ______                __                
   /  _/ __ \    /_  __/________ ______/ /_____  _____    
   / // /_/ /_____/ / / ___/ __ `/ ___/ //_/ _ \/ ___/    
 _/ // ____/_____/ / / /  / /_/ / /__/ ,< /  __/ /        
/___/_/         /_/ /_/   \__,_/\___/_/|_|\___/_/         
                                                 by xTyzenツIV
                      [!] Updated [!]""")

  time.sleep(1)

def ip():
  #code:
  Write.Print("\n[+] >> Please enter the victim's IP address: ", Colors.white_to_green, end='')
  ip_addr = input()
  print("\n")

  req1 = requests.get(f"http://ipinfo.io/{ip_addr}")
  req2 = requests.get(f"http://ip-api.com/json/{ip_addr}")
  req3 = requests.get(f"http://api.db-ip.com/v2/free/{ip_addr}")

  resp1 = req1.text
  resp2 = req2.text
  resp3 = req3.text

  Write.Print(f"[!] {resp3}", Colors.white_to_red)
  print("\n")
  Write.Print(f"[!] {resp1}", Colors.white_to_red)
  print("\n")
  Write.Print(f"[!] {resp2}", Colors.white_to_red)
  print("\n")
  Write.Print("[#] Results will be deleted in 25s [#]", Colors.blue_to_white)
  time.sleep(25)
  os.system("clear || cls")


while True:
  aff()
  ip()



