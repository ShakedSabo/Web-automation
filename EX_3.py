from selenium import webdriver

browser = webdriver.Chrome(executable_path="/home/shaked/homework/chromedriver")
browser.get('https://www.walla.co.il/')

firefox = webdriver.Firefox(executable_path="/home/shaked/homework/geckodriver")
firefox.get("https://www.walla.co.il/")
title = browser.title
title_2 = firefox.title
if title == title_2:
    print("Same")
else:
    print("Not The Same")

# it's the same locaters in different browsers