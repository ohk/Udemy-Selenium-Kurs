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
        Browser.amazonPageList(self)

    def amazonPageList(self):
        product_Names = self.browser.find_elements_by_xpath("//h2[@data-attribute]")
        link_List = []
        title = []
        for i in range(0, len(product_Names), 1):
            product_Description_Link = self.browser.find_element_by_xpath("//a[@title=\"{}\"]".format(product_Names[i].text))
            link_List.append(product_Description_Link.get_attribute("href"))
            title.append(product_Names[i].text)
        for i in range(0, len(product_Names), 1):
            self.browser.get(link_List[i])
            description = self.browser.find_element_by_id('feature-bullets').text
            text2 = ("\n\nTitle: {} \n-------------------------Description-------------------------\n{}\n\n").format(title[i],description)
            print(text2)
            file.FileFunctions(text2)
        self.browser.quit()
