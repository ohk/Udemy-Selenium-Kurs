from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Browser:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        driver_Path = "/Users/ohkamisli/Desktop/SeleniumKurs/chromedriver"
        self.browser = webdriver.Chrome(driver_Path)
        self.loginConfirm = False

    def loginInsta(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        username_field = self.browser.find_element_by_name("username")
        username_field.send_keys(self.username)
        password_field = self.browser.find_element_by_name("password")
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.ENTER)
        time.sleep(5)
        if self.browser.current_url != "https://www.instagram.com/accounts/login/":
            print("Giriş Başarılı olarak yapıldı ...")
            self.loginConfirm = True
        else:
            print("Giriş yapılamadı")
        try:
            time.sleep(7)
            self.browser.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
        except Exception as e:
            print(e)

    def followUser(self,fUserName):
        if self.loginConfirm == True:
            self.browser.get("https://www.instagram.com/" + fUserName)
            time.sleep(5)
            if self.browser.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button").text == "Follow":
                self.browser.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button").click()
                print("Takip edilen kullanıcı: " + fUserName)
            else:
                print("Kullanıcı takip edilemedi...")
        else:
            print("Giriş yapılamadı... Bu fonksiyonu çalıştıramıyorum...")

    def unfollowUser(self,fUserName):
        if self.loginConfirm == True:
            self.browser.get("https://www.instagram.com/" + fUserName)
            time.sleep(5)
            if self.browser.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button").text == "Following":
                self.browser.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button").click()
                time.sleep(5)
                self.browser.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[1]").click()
                print("Takipten vazgeçilen kullanıcı: " + fUserName)
            else:
                print("Kullanıcı takip edilmiyor...")
        else:
            print("Giriş yapılamadı... Bu fonksiyonu çalıştıramıyorum...")

    def likePhoto(self,link):
        if self.loginConfirm == True:
            self.browser.get(link)
            try:
                likeB = self.browser.find_element_by_xpath("//button[./span[@aria-label=\"Like\"]]").click()
                print("Fotoğraf beğenildi... Link:" + link)
            except Exception as e:
                print("Bu fotoğraf beğenilmiş...")

    def unlikePhoto(self,link):
        if self.loginConfirm == True:
            self.browser.get(link)
            try:
                likeB = self.browser.find_element_by_xpath("//button[./span[@aria-label=\"Unlike\"]]").click()
                print("Fotoğraf beğenmekten vazgeçildi ... Link:" + link)
            except Exception as e:
                print("Bu fotoğraf beğenilmemiş...")

    def likeBomb(self, fUserName):
        if self.loginConfirm == True:
            self.browser.get("https://www.instagram.com/" + fUserName)
            Browser.scrollPage(self)
            list = self.browser.find_elements_by_xpath("//div[contains(@class, 'v1Nh3 kIKUG  _bz0w')]/a")
            list2 =[]
            for x in list:
                list2.append(x.get_attribute("href"))
                print("Listeye Eklendi: " + x.get_attribute("href"))
            for x in list2:
                Browser.likePhoto(self,link = x)

    def scrollPage(self):
        SCROLL_PAUSE_TIME = 0.5

        # Get scroll height
        last_height = self.browser.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
