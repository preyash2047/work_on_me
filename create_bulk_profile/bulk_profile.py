from gologin import GoLogin
import pandas as pd
import random
import time
from faker import Faker

fake = Faker()

global obj
obj = GoLogin(options={
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MThiYTdmN2RiYmM5MzNlODNkYmM5ZjkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MThiYTgxNWRiYmM5MzU1MzlkYmNhMDcifQ.pQueIhjVztexcwzNCSHxu-4X1tvcf5eqFtHFBzYn7X0",
    "profile_id": "618ba7f8dbbc936b21dbc9fb"
})

orignalDataset = pd.read_csv("profile_dataset_2.csv")
dataset = orignalDataset[orignalDataset['proxyList'].notnull(
)][orignalDataset['isCreated'] != True]

for i in range(len(dataset.proxyList)):
    host, port = dataset.proxyList.iloc[i].split(":")
    options = {
        "name": str(fake.name()),
        "notes": "",
        "debugMode": False,
        "browserType": "chrome",
        "os": random.choice(["win", "android", "mac", "lin"]),
        "startUrl": random.choice(["google.com", "coindesk.com", "markets.businessinsider.com", "coinbase.com", "economictimes.indiatimes.com"]),
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
    if(resultID != None):
        print("No Profiles created successfully:", i+1)
        index = orignalDataset.index[orignalDataset['proxyList'] == dataset.proxyList.iloc[i]]
        # orignalDataset.isCreated.iloc[index] = True

orignalDataset.to_csv("profile_dataset_2.csv", index=False)
print("Profile Creation Done")