from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep



browser = webdriver.Chrome(executable_path="/home/shaked/homework/chromedriver")
browser.get("https://www.youtube.com/")
sleep(2)
browser.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("sunday morning")
browser.find_element(by=By.ID, value='search-icon-legacy').click()

