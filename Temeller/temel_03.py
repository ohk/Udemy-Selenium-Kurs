from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

driver_Path = "/Users/ohkamisli/Desktop/SeleniumKurs/chromedriver"
driver = webdriver.Chrome(driver_Path)
driver.get("https://www.python.org/")
search_Query = driver.find_element_by_xpath("//input[@id=\"id-search-field\"]")
search_Query.send_keys("pycon")
driver.find_element_by_xpath("//*[@id=\"submit\"]").click()
time.sleep(5)
driver.quit()
