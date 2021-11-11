from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from gologin import GoLogin
from sys import platform
import pandas as pd
import random
import time

global gl
gl = GoLogin({
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MTgwMWEwMGQ2ODA0NTIwYmI0MzgwNTYiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MTgxNmM2NzY3MWZiMWVhMGM1ZjRiNzMifQ.t_NhbA76YRkay1lo4bJUBC6ct0Qc4GhCb58e6nyTIGk",
	"profile_id": "6186cd2cbef6f731e8c27a2d",
	})

print(gl.getProfile())
exit()

if platform == "linux" or platform == "linux2":
	chrome_driver_path = "./chromedriver"
elif platform == "darwin":
	chrome_driver_path = "./mac/chromedriver"
elif platform == "win32":
	chrome_driver_path = "chromedriver.exe"

profileIds = gl.getProfileIdList()
profileIds = profileIds[:1]

orignalDataset = pd.read_csv("users_data.csv")
dataset = orignalDataset[orignalDataset['name'].notnull()]

for i in profileIds:
    gl.profile_id = i
    debugger_address = gl.start()
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", debugger_address)
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    driver.close()
    time.sleep(5)
    gl.stop()

exit()
for i in profileIds:
    host, port = dataset.proxyList.iloc[i].split(":")
    options = {
        "name": dataset.name.iloc[i],
        "notes": "",
        "debugMode": False,
        "browserType": "chrome",
        "os": random.choice(["win","android","mac","lin"]),
        "startUrl": random.choice(["google.com","coindesk.com","markets.businessinsider.com","coinbase.com","economictimes.indiatimes.com"]),
        "googleServicesEnabled": random.choice([True, False]),
        "lockEnabled": random.choice([True, False]),
        "audioContext": {
            "mode": "noise"
        },
        "canvas": {
            "mode": "noise"
        },
        "webRTC": {
            "mode": "disabled",
            "enabled": random.choice([True, False]),
            "customize": random.choice([True, False]),
            "fillBasedOnIp": random.choice([True, False])
        },
        "proxyEnabled": True,
        "proxy": {
            "mode": "http",
            "host": host,
            "port": port,
        }
    }
    resultID = obj.create(options)
    time.sleep(2)
    print("resultID", resultID)
    print("No Profiles created successfully:",i+1 )
    index = orignalDataset.index[orignalDataset['proxyList'] == dataset.proxyList.iloc[i]]
    orignalDataset.isCreated.iloc[index] = True

orignalDataset.to_csv("profile_dataset_2.csv", index=False)