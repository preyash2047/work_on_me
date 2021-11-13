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

global gl
gl = GoLogin(options={
    "token": get_key(),
    "profile_id": ""
})

if platform == "linux" or platform == "linux2":
	chrome_driver_path = "./chromedriver"
elif platform == "darwin":
	chrome_driver_path = "./mac/chromedriver"
elif platform == "win32":
	chrome_driver_path = "chromedriver.exe"

def getProfileIdList(obj):
    headers = {'Authorization': 'Bearer ' + str(obj.access_token)}
    response = requests.request("GET", "https://api.gologin.com/browser/", headers=headers, data={})
    return [i["id"] for i in json.loads(response.text)]

profileIds = getProfileIdList(gl)
profileIds = profileIds[1:3]

orignalDataset = pd.read_csv("users_data.csv")
dataset = orignalDataset[orignalDataset['name'].notnull()]

for i in profileIds:
    gl.profile_id = i
    debugger_address = gl.start()
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", debugger_address)
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    driver = CodeMe(driver)
    driver = driver.start()
    time.sleep(30)
    driver.close()
    gl.stop()

print("Python File Execution Finished")