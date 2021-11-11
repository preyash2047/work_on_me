import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin

gl = GoLogin({
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MTgwMWEwMGQ2ODA0NTIwYmI0MzgwNTYiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MTgxNmM2NzY3MWZiMWVhMGM1ZjRiNzMifQ.t_NhbA76YRkay1lo4bJUBC6ct0Qc4GhCb58e6nyTIGk",
    "profile_id": "61802652089b4a47d81c9d06"
	})

gl.start()
exit()

if platform == "linux" or platform == "linux2":
	chrome_driver_path = "./chromedriver"
elif platform == "darwin":
	chrome_driver_path = "./mac/chromedriver"
elif platform == "win32":
	chrome_driver_path = "chromedriver.exe"

debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
driver.get("http://www.python.org")
assert "Python" in driver.title
driver.close()
time.sleep(3)
gl.stop()