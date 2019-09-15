import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import os

import firebase_admin
from firebase_admin import credentials, db
from firebase import firebase

def fb_login_scrape(username, email, password):
    option_chrome = webdriver.ChromeOptions()
    option_chrome.add_argument('headless')
    option_chrome.add_argument("disable-gpu")
    option_chrome.add_argument("--disable-infobars")
    option_chrome.add_argument("--disable-extensions")

    path = r"/Users/lauradang/social-media/chromedriver"

    url = "https://facebook.com"
    fb_driver = webdriver.Chrome(executable_path=path, options=option_chrome)
    fb_driver.get(url)

    fb_driver.find_element_by_xpath("//input[@id='email']").send_keys(email)
    fb_driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
    time.sleep(4)
    fb_driver.find_element_by_xpath("//input[@id='u_0_2']").click()
    time.sleep(2)
    link = fb_driver.find_element_by_xpath("//a[@accesskey='2']").get_attribute('href')

    app = firebase.FirebaseApplication("https://social-media-app-e8fe0.firebaseio.com/")

    obj = app.get('/users', None)[username]
    obj.update({"fb_link":link})
    app.put('users', username, obj)

    return fb_driver

def fb_add_friend(fb_driver, friend_username, username):
    app = firebase.FirebaseApplication("https://social-media-app-e8fe0.firebaseio.com/")
    url = app.get('/users', None)[friend_username]['fb_link']
    fb_driver.get(url)
    time.sleep(2)
    fb_driver.find_elements_by_tag_name("button")[1].click()

