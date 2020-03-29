from selenium import webdriver
import csvCreator

class Browser:
    def __init__(self):
        driver_Path = "/Users/ohkamisli/Desktop/SeleniumKurs/chromedriver"
        self.browser = webdriver.Chrome(driver_Path)
        csvCreator.csvCretor.csvCreate(self)
        Browser.goIMDB(self)

    def goIMDB(self):
        self.browser.get("https://www.imdb.com/chart/top")
        Browser.listMovies(self)

    def listMovies(self):
        for i in range(1, 251, 1):
            movie_name = self.browser.find_element_by_xpath("//*[@id=\"main\"]/div/span/div/div/div[3]/table/tbody/tr["+str(i)+"]/td[2]/a").get_attribute("innerHTML")
            url = self.browser.find_element_by_xpath("//*[@id=\"main\"]/div/span/div/div/div[3]/table/tbody/tr["+str(i)+"]/td[2]/a")
            Browser.getData(self, movie_name, url.get_attribute("href"))

    def getData(self, movie_name, url):
        self.browser.get(url)
        data = self.browser.find_element_by_xpath("//*[@id=\"titleStoryLine\"]/div[1]/p/span")
        csvCreator.csvCretor.csvWriteRow(self, movie_description=data.get_attribute("innerHTML"), movie_link = url , movie_name=movie_name)
        self.browser.get("https://www.imdb.com/chart/top")
