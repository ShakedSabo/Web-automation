from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path="/home/shaked/homework/chromedriver")
browser.get('https://translate.google.co.il/?hl=iw&sl=iw&tl=en&op=translate')
browser.find_element(by=By.ID, value='yDmH0d').send_keys("שלום")
