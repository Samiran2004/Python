import os
import logging
import datetime
import json
import shutil
import re
import requests

## Check valid URL using regular expression
def isValidUrl(url):
    patternt = re.compile(
        r'^(https?:\/\/)?' # http:// or https:// (optional)
        # r'(www\.)?' # www. (optional)
        # r'([a-zA-Z0-9]+(\.[a-zA-Z0-9]+)+)' # domain
        # r'(\/[a-zA-Z0-9-._~:/?#[\]@!$&\'()*+,;=]*)?' # path (optional)
        # r'$'
    )
    return bool(re.match(patternt, url))

## Make request...
def make_request(url):
    try:
        response = requests.get(url, timeout=20)
        logging.info(f"Successful request")
        return response.status_code
    except:
        logging.warning(f"Unsuccessful request")
        return False


## Take input from user...
url: str = str(input("Enter the url: "))

if not isValidUrl(url):
    print(f"{url} is not a valid URL...")
    exit()

try:
    reqNum = int(input("Enter the number of requests: "))
except ValueError:
    print("Not a valid value...")
    reqNum=1000
    print(f"{reqNum} set as default request...")

## Setup logging...
if not os.path.exists("logs"):
    print("Create logs folder...")
    os.mkdir("logs")

logsFileName = url.replace("https://", "")

logging.basicConfig(filename=f"logs/{logsFileName}.log", level=logging.INFO, format="%(asctime)s - %(message)s")

count=1

while count <= reqNum:
    make_request(url)
    count += 1