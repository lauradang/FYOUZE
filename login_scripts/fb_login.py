import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

option_chrome = webdriver.ChromeOptions()
option_chrome.add_argument('headless')
option_chrome.add_argument("disable-gpu")

path = "/Users/lauradang/fippa-cleaning/chromedriver"

url = "https://facebook.com"
fb_driver = webdriver.Chrome(executable_path=path)
fb_driver.get(url)

fb_driver.find_element_by_xpath("//input[@id='email']").send_keys("lauradang.2000@gmail.com")
fb_driver.find_element_by_xpath("//input[@type='password']").send_keys("9087UreSa47")
time.sleep(1)
fb_driver.find_element_by_xpath("//input[@id='u_0_2']").click()