from selenium import webdriver
import file


class Browser:
    def __init__(self, link):
        driver_Path = "/Users/ohkamisli/Desktop/SeleniumKurs/chromedriver"
        self.browser = webdriver.Chrome(driver_Path)
        self.link = link
        Browser.goAmazon(self)

    def goAmazon(self):
        self.browser.get(self.link)
        Browser.AmazonPageList(self)

    def AmazonPageList(self):
        product_Prices = self.browser.find_elements_by_class_name('a-offscreen')
        product_Names = self.browser.find_elements_by_xpath("//h2[@data-attribute]")
        for i in range(0, len(product_Prices), 1):
            text = "{} - Product Name: {}- Price: {}".format(i+1, product_Names[i].text, product_Prices[i].get_attribute("innerHTML"))
            print(text)
            file.FileFunctions(text)
        self.browser.quit()
