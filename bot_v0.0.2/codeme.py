import time

class CodeMe:
    def __init__(self,driver):
        self.driver = driver
    def start(self):
        print("I will perform my Task")
        self.driver.get("https://sweepwidget.com/view/39390-r8jw31kl")
        time.sleep(30)
        content = self.driver.page_source
        print(":content:"*20,"\n", content)
        return self.driver