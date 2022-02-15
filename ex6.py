from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(executable_path="/home/shaked/homework/chromedriver")
browser.get("https://translate.google.co.il/?hl=iw")
A = browser.find_element_by_class_name("er8xn")
B = browser.find_element_by_id("yDmH0d")
C = browser.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea")
