from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from datetime import date
from faker import Faker
import hashlib
import random
import time

fake = Faker()

#Bot Configeration
referalName = "Preyash"
userName = str(fake.name())
userEmail = str(fake.email(domain=random.choice(["gmail.com", "yahoo.com", "hotmail.com"])))
UserProfileName = "preyash12"
referalURL = "https://sweepwidget.com/view/40066-oqpecwsz"

randomSleepOnEveryActionStart = 3
randomSleepOnEveryActionEnd = 5
randomSleepOnEveryTaskActionStart = 5
randomSleepOnEveryTaskActionEnd = 10
pageChangeTimeStart = 5
pageChangeTimeEnd = 10


def mainPage(driver, name, email):
    # bscWallet = hashlib.sha256(bytes(f"{date.today()}", 'utf-8')).hexdigest()[:42]
    #name
    input1 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[3]/div[2]/div[1]/input")
    input1.send_keys(name)
    
    time.sleep(random.randint(randomSleepOnEveryActionStart, randomSleepOnEveryActionEnd))
    
    #email
    input2 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[3]/div[2]/div[2]/input")
    input2.send_keys(email)
    
    # time.sleep(random.randint(randomSleepOnEveryActionStart, randomSleepOnEveryActionEnd))

    # #bsc
    # input3 = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div[3]/div/div[3]/div/div/div/div/input")
    # input3.send_keys(bscWallet)
   
    # time.sleep(random.randint(randomSleepOnEveryActionStart, randomSleepOnEveryActionEnd))
    
    #submit
    time.sleep(3)
    input2.send_keys(Keys.ENTER)

class CodeMe:
    def __init__(self,driver):
        self.driver = driver

    def start(self):
        # print("I will perform my Task")

        self.driver.get(referalURL)
        time.sleep(5)
        
        mainPage(self.driver, str(fake.name()), self.emails[0])
        self.emails = self.emails[1:]
        time.sleep(random.randint(10,30))

        return self.driver