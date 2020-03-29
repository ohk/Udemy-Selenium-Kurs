from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver_Path = "/Users/ohkamisli/Desktop/SeleniumKurs/chromedriver"
driver = webdriver.Chrome(driver_Path)
driver.get("https://www.python.org/")
search_Field = driver.find_element_by_id('id-search-field')
search_Field.send_keys("İlk Deneme")
search_Field.send_keys(Keys.RETURN)
time.sleep(5)
search_Field2 = driver.find_element_by_name('q')
search_Field2.clear()
time.sleep(2)
search_Field2.send_keys("İkinci Deneme")
go_Button = driver.find_element_by_name("submit")
go_Button.click()
time.sleep(5)
driver.quit()
