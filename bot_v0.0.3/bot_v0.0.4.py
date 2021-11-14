from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from gologin import GoLogin
from codeme import CodeMe
from sys import platform
import pandas as pd
from get_key import get_key
import random
import time
import requests
import json
from faker import Faker

fake = Faker()

global gl
gl = GoLogin(options={
    # "token": get_key(),
    "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MTkxMDRkZGNjZGU0NTVjZTJlZjgzNWUiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MTkxMDRlOWFmNzVkYjg4NWM0YTJmNzkifQ.EqT2rBmnY6U2Ie3zwW1QGSobahdxL0gKW9-V5NA7TYo",
    "profile_id": "619104ddccde456b12ef8360"
})


chrome_driver_path = "chromedriver.exe"

for i in range(10):
    gl.setProfileId("619104ddccde456b12ef8360")

    # gl.update(    options = {
    #     "name": str(fake.name()),
    #     "notes": "",
    #     "debugMode": False,
    #     "browserType": "chrome",
    #     "os": random.choice(["win", "android", "mac", "lin"]),
    #     "startUrl": random.choice(["google.com", "coindesk.com", "markets.businessinsider.com", "coinbase.com", "economictimes.indiatimes.com"]),
    #     "googleServicesEnabled": random.choice([True, False]),
    #     "lockEnabled": random.choice([True, False]),
    #     "audioContext": {
    #         "mode": "noise"
    #     },
    #     "canvas": {
    #         "mode": "noise"
    #     },
    #     "webRTC": {
    #         "mode": "disabled",
    #         "enabled": random.choice([True, False]),
    #         "customize": random.choice([True, False]),
    #         "fillBasedOnIp": random.choice([True, False])
    #     },
    # })

    debugger_address = gl.start()
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", debugger_address)
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    driver = CodeMe(driver)
    try:
        driver = driver.start()
        driver.close()  
    except:
        pass
    gl.stop()

print("Python File Execution Finished")
