from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import date
import os
from fake_useragent import UserAgent
import random

if(not os.path.isfile('chromedriver.exe')):
    print("Download Chrome Driver from this url as per your chrome version: 'https://chromedriver.chromium.org/downloads' and put it in same folder named as 'chromedriver.exe'")
    time.sleep(120)
    exit()

if(not os.path.isfile('data.txt')):
    print("get sample 'data.txt' and put it in same folder")
    time.sleep(120)
    exit()    
    
text = open("data.txt", 'r').read().split()

ua = UserAgent()

for t in range(3):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"user-agent={ua.chrome}")
    chrome_options.add_argument(f"--width={random.randint(1200,1500)}")
    chrome_options.add_argument(f"--height={random.randint(1200,1500)}")
    # chrome_options.add_argument('--proxy-server=%s' % t)
    chrome = webdriver.Chrome('chromedriver.exe',chrome_options=chrome_options)
    chrome.get(text[0])
    time.sleep(int(text[1]))

exit()