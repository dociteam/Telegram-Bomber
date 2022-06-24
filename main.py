# Telegram Bomber - DociTeam
# YouTube Video : https://youtu.be/pWHHpnPz0jc

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import os
import time

def clear_console():
    if os.name in ('nt', 'dos'): #Check OS name for using correct command
        try:
            os.system("cls")
        except:
            pass
    else:
        try:
            os.system("clear")
        except:
            pass

def change_title():
    if os.name in ('nt', 'dos'):
        try:
            os.system('title "DociTeam | Telegram Bomber"')
        except:
            pass
    else:
            pass


clear_console()
change_title()

class color : 
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    Default = '\033[99m'

dociteam = color.Cyan+"""
                                     ____             _ _____                    
                                    |  _ \  ___   ___(_)_   _|__  __ _ _ __ ___  
                                    | | | |/ _ \ / __| | | |/ _ \/ _` | '_ ` _ \ 
                                    | |_| | (_) | (__| | | |  __/ (_| | | | | | |
                                    |____/ \___/ \___|_| |_|\___|\__,_|_| |_| |_|
"""
def slowprint(text: str, speed: float, newLine=True):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)
    if newLine:
        print()

print(dociteam)
time.sleep(2)
slowprint(color.Yellow+f"\n\n|---------- Welcome to {color.Blue}Telegram {color.Red}Bomber{color.Yellow}! ----------|\n",0.07)
slowprint(color.Yellow+"[!] This Project is Education Purpose Only!\n",0.07)

API_ID = int(input(color.Yellow+"[+] Enter Your API_ID : "+color.White))
API_HASH = str(input(color.Yellow+"[+] Enter Your API_HASH : "+color.White))
PHONE = str(input(color.Yellow+"[+] Enter Your Phone Number With Country Code (Ex : +12345...) : "+color.White))
TARGET = str(input(color.Yellow+"[+] Enter Target's Phone Number Or ID Or Group Invite Link : "+color.White)) #ID Ex : @dociteam
MESSAGE = str(input(color.Yellow+"[+] Enter Your Message : "+color.White))
COUNTER = int(input(color.Yellow+"[+] How Many Messages Do You Want To Send? : "+color.White))

client = TelegramClient('session',API_ID, API_HASH)
client.start()
print(color.Green+"[+] Lets Start...\n")

async def main():
    if not await client.is_user_authorized():
        await client.send_code_request(PHONE)
        try:
            await client.sign_in(PHONE, input(color.Yellow+'[+] Enter the code : '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input(color.Yellow+'[+] Password : '))
    for i in range(1,int(COUNTER) + 1):
        await client.send_message(TARGET, MESSAGE)
        print(color.Green+"[+] Message Has Sent!\n")
    input(color.Green+'\nPress Enter To Quit........')

with client:
    client.loop.run_until_complete(main())