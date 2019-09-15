import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import os

import firebase_admin
from firebase_admin import credentials, db
from firebase import firebase

def ig_login_scrape(username, email, password):
    option_chrome = webdriver.ChromeOptions()
    option_chrome.add_argument('headless')
    option_chrome.add_argument("disable-gpu")

    path = r"/Users/lauradang/social-media/chromedriver"

    url = "https://www.instagram.com/accounts/login/?source=auth_switcher"
    ig_driver = webdriver.Chrome(executable_path=path, options=option_chrome)
    ig_driver.get(url)

    time.sleep(2)
    ig_driver.find_element_by_xpath("//input[@name='username']").send_keys(email)
    ig_driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    time.sleep(1)
    ig_driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(3)

    try:
        ig_driver.find_element_by_xpath("//button[text()='Not Now']").click()
    except NoSuchElementException:
        pass

    time.sleep(2)
    link = ig_driver.find_element_by_xpath("//span[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[3]/a").get_attribute('href')

    app = firebase.FirebaseApplication("https://social-media-app-e8fe0.firebaseio.com/")

    obj = app.get('/users', None)[username]
    obj.update({"ig_link":link})
    app.put('users', username, obj)

    return ig_driver

def ig_add_friend(ig_driver, friend_username, username):
    app = firebase.FirebaseApplication("https://social-media-app-e8fe0.firebaseio.com/")
    url = app.get('/users', None)[friend_username]['ig_link']

    ig_driver.get(url)
    time.sleep(3)

    ig_driver.find_element_by_xpath("//span[@id='react-root']/section/main/div/header/section/div[1]/div[1]/span/span[1]/button").click()
