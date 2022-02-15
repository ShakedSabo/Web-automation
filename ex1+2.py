from selenium import webdriver

browser = webdriver.Chrome(executable_path="/home/shaked/homework/chromedriver")
browser.get('https://www.walla.co.il/')

firefox = webdriver.Firefox(executable_path="/home/shaked/homework/geckodriver")
firefox.get("https://www.ynet.co.il/home/0,7340,L-8,00.html")
#exercise 2
title = browser.title
browser.refresh()
if title == browser.title:
    print("Same")
else:
    print("Not The Same")
