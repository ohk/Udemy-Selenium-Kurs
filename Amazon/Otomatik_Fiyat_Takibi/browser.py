from selenium import webdriver
import time


class Browser:
    def __init__(self, time, count, link):
        driver_Path = "/Users/ohkamisli/Desktop/SeleniumKurs/chromedriver"
        self.browser = webdriver.Chrome(driver_Path)
        self.time = time
        self.count = count
        self.link = link
        Browser.goAmazon(self)

    def goAmazon(self):
        self.browser.get(self.link)
        Browser.checkPrice(self)

    def checkPrice(self):
        for x in range(0, self.count, 1):
            price = self.browser.find_element_by_id('price_inside_buybox')
            print("Price: " + price.text)
            time.sleep(self.time)
        self.browser.quit()
