from gologin import GoLogin
import pandas as pd
import random
import time
from faker import Faker

fake = Faker()

global obj
obj = GoLogin(options={
    # "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MThiYTdmN2RiYmM5MzNlODNkYmM5ZjkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MThiYTgxNWRiYmM5MzU1MzlkYmNhMDcifQ.pQueIhjVztexcwzNCSHxu-4X1tvcf5eqFtHFBzYn7X0",
    "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MTkxMDRkZGNjZGU0NTVjZTJlZjgzNWUiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MTkxMDRlOWFmNzVkYjg4NWM0YTJmNzkifQ.EqT2rBmnY6U2Ie3zwW1QGSobahdxL0gKW9-V5NA7TYo",
    "profile_id": "618ba7f8dbbc936b21dbc9fb"
})

dataset_path= "profile_dataset_2.csv"
orignalDataset = pd.read_csv(dataset_path)
dataset = orignalDataset[orignalDataset['proxyList'].notnull(
)][orignalDataset['isCreated'] != True]

def getOptions(i):
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
    
    if(resultID != None):
        index = orignalDataset.index[orignalDataset['proxyList'] == dataset.proxyList.iloc[i]]
        orignalDataset.isCreated.iloc[index] = True
    
    return resultID

print("Profiles created successfully:\n")
for i in range(len(dataset.proxyList)):
    try:
        resultID = getOptions(i)
        print(i+1, end=" ")
    except:
        print("Failed to Create Profile number", i+1)
    finally:
        time.sleep(.5)
        # pass

orignalDataset.to_csv(dataset_path, index=False)
print("Profile Creation Done")