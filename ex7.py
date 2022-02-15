from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome(executable_path="/home/shaked/homework/chromedriver")
browser.get("https://www.facebook.com/")
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
wait = WebDriverWait(browser, 10)
wait.until(EC.title_contains('Log'))
email = browser.find_element_by_id("email").send_keys("Shaked")
sleep(1)
paasword = browser.find_element_by_id("pass").send_keys("Sabo")
sleep(1)
enter = browser.find_element_by_name("login").click()
