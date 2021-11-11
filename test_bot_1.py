from gologin import GoLogin
import pandas as pd
import random
import time

global obj
obj = GoLogin(options={
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MTgwMWEwMGQ2ODA0NTIwYmI0MzgwNTYiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MTgxNmM2NzY3MWZiMWVhMGM1ZjRiNzMifQ.t_NhbA76YRkay1lo4bJUBC6ct0Qc4GhCb58e6nyTIGk",
    "profile_id": "61802652089b4a47d81c9d06"
})

fileName = "profile_dataset.xlsx"
name = pd.read_excel(fileName, sheet_name="nameAndStrtUrl").name.dropna()
strtUrl = pd.read_excel(
    fileName, sheet_name="nameAndStrtUrl").startUrl.dropna()
userAgentAndOs = pd.read_excel(fileName, sheet_name="userAgentAndOs").dropna()
screenSize = pd.read_excel(fileName, sheet_name="screenSize").dropna()
proxyList = pd.read_excel(fileName, sheet_name="proxyList").dropna()
dataset = pd.DataFrame(
    columns=["name", "os", "screenHeight", "screenWidth", "userAgent", "host", "port"])

for i in range(len(name)):
    randomUserAgent = userAgentAndOs.sample()
    if(randomUserAgent.os.iloc[0] == "android"):
        randomScreenSize = screenSize[screenSize.isMobile == True].sample()
    else:
        randomScreenSize = screenSize[screenSize.isMobile == False].sample()
    host, port = proxyList.proxyList.iloc[i].split(":")
    rowData = {
        "name": name.iloc[i],
        "os": randomUserAgent.os.iloc[0],
        "screenHeight": randomScreenSize.height.iloc[0],
        "screenWidth": randomScreenSize.width.iloc[0],
        "userAgent": randomUserAgent.userAgent.iloc[0],
        "host": str(host),
        "port": eval(port)
    }
    dataset = dataset.append(rowData, ignore_index=True)

# for i in range(len(dataset)):
# for i in range(0, 2):
i = 0

options = {
    "name": dataset.name.iloc[i],
    "notes": "",
    "debugMode": False,
    "browserType": "chrome",
    "os": dataset.os.iloc[i],
    "startUrl": random.choice(strtUrl),
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
    # "screenHeight": dataset.screenHeight.iloc[i],
    # "screenWidth": dataset.screenWidth.iloc[i],
    # "navigator.resolution" : f"{dataset.screenWidth.iloc[i]}x{dataset.screenHeight.iloc[i]}",
    "proxyEnabled": True,
    # "navigator.userAgent":"dataset.userAgent.iloc[i]",
    "proxy": {
        "mode": "http",
        "host": dataset.host.iloc[i],
        "port": dataset.port.iloc[i],
    }
}
print("options", options)
resultID = obj.create(options)
# print("options",options)
# time.sleep(10)
print("resultID", resultID)
# print("No Profiles created successfully:",i+1 )

# obj.start()
# obj.stop()
