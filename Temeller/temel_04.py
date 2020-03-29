from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

driver_Path = "/Users/ohkamisli/Desktop/SeleniumKurs/chromedriver"
driver = webdriver.Chrome(driver_Path)
driver.get("https://www.python.org/")
driver.find_element_by_partial_link_text('Success').click()
time.sleep(5)
driver.find_element_by_link_text('About').click()
time.sleep(5)
driver.quit()
