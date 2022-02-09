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
    # "token": get_key(),
    "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MTkxMDRkZGNjZGU0NTVjZTJlZjgzNWUiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MTkxMDRlOWFmNzVkYjg4NWM0YTJmNzkifQ.EqT2rBmnY6U2Ie3zwW1QGSobahdxL0gKW9-V5NA7TYo",
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
notWorking = None
with open("notWorkingProfileId.txt","r") as f:
    notWorking = f.read()
notWorking = notWorking.split("\n")[:-1]
profileIds = [i for i in profileIds if i not in notWorking]
# profileIds = profileIds[1:3]
# profileIds = ["618f8d89e22533478d58c5ed"]



for i in profileIds:
    gl.setProfileId(i)
    debugger_address = gl.start()
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", debugger_address)
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    driver = CodeMe(driver)
    try:
        driver = driver.start()
        # time.sleep(5)
        if "1 more way to enter." in driver.page_source:
            with open("workingProfileId.txt", "a") as f:
                f.write(i + "\n")
        driver.close()  
    except:
        with open("notWorkingProfileId.txt", "a") as f:
            f.write(i + "\n")
    gl.stop()

print("Python File Execution Finished")
