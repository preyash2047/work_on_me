from gologin import GoLogin
import pandas as pd
import random
import time

global obj
obj = GoLogin(options={
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MTgwMWEwMGQ2ODA0NTIwYmI0MzgwNTYiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MTgxNmM2NzY3MWZiMWVhMGM1ZjRiNzMifQ.t_NhbA76YRkay1lo4bJUBC6ct0Qc4GhCb58e6nyTIGk",
    "profile_id": "6187648ecbd4ec3e1a2ff11e"
})
obj.start()
# print(obj.create())

exit()
orignalDataset = pd.read_csv("profile_dataset_2.csv")
dataset = orignalDataset[orignalDataset['name'].notnull()][orignalDataset['isCreated'] != True]

for i in range(len(dataset.name)):
    host, port = dataset.proxyList.iloc[i].split(":")
    options = {
        "name": dataset.name.iloc[i],
        # "notes": "",
        # "debugMode": False,
        # "browserType": "chrome",
        # "os": random.choice(["win", "android", "mac", "lin"]),
        # "startUrl": random.choice(["google.com", "coindesk.com", "markets.businessinsider.com", "coinbase.com", "economictimes.indiatimes.com"]),
        # "googleServicesEnabled": random.choice([True, False]),
        # "lockEnabled": random.choice([True, False]),
        # "audioContext": {
        #     "mode": "noise"
        # },
        # "canvas": {
        #     "mode": "noise"
        # },
        # "webRTC": {
        #     "mode": "disabled",
        #     "enabled": random.choice([True, False]),
        #     "customize": random.choice([True, False]),
        #     "fillBasedOnIp": random.choice([True, False])
        # },
        # "proxyEnabled": True,
        # "proxy": {
        #     "mode": "http",
        #     "host": host,
        #     "port": port,
        # }
    }
    resultID = obj.create(options)
    time.sleep(2)
    print("resultID", resultID)
    if(resultID != None):
        print("No Profiles created successfully:", i+1)
        index = orignalDataset.index[orignalDataset['proxyList'] == dataset.proxyList.iloc[i]]
        orignalDataset.isCreated.iloc[index] = True

orignalDataset.to_csv("profile_dataset_2.csv", index=False)