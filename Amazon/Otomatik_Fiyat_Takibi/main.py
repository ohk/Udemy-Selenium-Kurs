import browser

link = input("Lütfen ürün linkini giriniz \n\t>")
count = int(input("Kaç kere fiyat kontrol edilecek? \n\t>"))
time = int(input("Her kontrol arasında kaç saniye beklenecek? \n\t>"))
browser = browser.Browser(time=time, count=count, link=link)
