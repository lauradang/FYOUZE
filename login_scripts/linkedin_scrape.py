from bs4 import BeautifulSoup
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import firebase
from firebase import firebase

def linkedin_login_scrape(username, email, password):
    option_chrome = webdriver.ChromeOptions()
    option_chrome.add_argument('headless')
    option_chrome.add_argument("disable-gpu")

    path = r"/Users/lauradang/social-media/chromedriver"

    url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
    linkedin_driver = webdriver.Chrome(executable_path=path, options=option_chrome)
    linkedin_driver.get(url)
    linkedin_driver.find_element_by_xpath("//input[@id='username']").send_keys(email)
    linkedin_driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
    time.sleep(1)
    linkedin_driver.find_element_by_xpath("//button[@type='submit']").click()

    time.sleep(4)

    soup = BeautifulSoup(linkedin_driver.page_source, 'lxml')
    link = "https://www.linkedin.com" + soup.find("a", {"class":"tap-target block link-without-hover-visited ember-view"})['href']

    app = firebase.FirebaseApplication("https://social-media-app-e8fe0.firebaseio.com/")

    obj = app.get('/users', None)[username]
    obj.update({"linkedin_link":link})
    app.put('users', username, obj)
    return linkedin_driver

def linkedin_add_friend(linkedin_driver, friend_username, username):
    app = firebase.FirebaseApplication("https://social-media-app-e8fe0.firebaseio.com/")
    url = app.get('/users', None)[friend_username]['linkedin_link']
    print(url)
    linkedin_driver.get(url)
    time.sleep(3)

    linkedin_driver.find_element_by_xpath("//*[text()='Connect']").click()
    try:
        linkedin_driver.find_element_by_xpath("//*[text()='Send invitation']").click()
    except:
        pass