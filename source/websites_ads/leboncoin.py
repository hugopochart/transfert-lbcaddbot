# coding: utf-8

import adbot_utils
import time
import os

from tkinter import *
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

login = "hugo.pochart@gmail.com"
login_id = "st_username"
login_url = "https://www.leboncoin.fr/"
password = "zoom1996"
password_id = "st_passwd"

def post_ad(browser, begin, end, ads):
    website_login(browser)
    size = len(ads) # to know the number of ads
    for x in range(begin, end):
        print(f"AD [{x + 1}/{size}]")
        # T.insert(END, f"\nAD [{x + 1}/{size}] -- ({ads[x][0]})")
        # T.pack(side=TOP)
        # fenetre.update()
        size_localisation = len(ads[x][3])
        adbot_utils.get_page(browser, "https://www.leboncoin.fr/ai?ca=12_s", By.ID, "formular") #go to post ad web page
        WebDriverWait(browser, 5).until(ec.presence_of_element_located(
            (By.ID, "subject")))
        fill_form(browser, ads[x]) # fill the form to post an ad with a hash composed of info about the ad
        upload_images(browser, os.getcwd(), "123")# upload images for the ad
        post(browser) # post the ad
        browser.save_screenshot("debug/validation_" + ads[x][0]+ ".png") # get scrrenshot confirmation
# used to go to log in form
def get_login_form(browser):
    browser.get(login_url)
    try:
        WebDriverWait(browser, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@title='Accéder à mon compte']")))
    except TimeoutException:
        get_login_form(browser, T, fenetre)
    browser.find_element_by_xpath("//button[@title='Accéder à mon compte']").click()
    adbot_utils.print_log("Login page loaded", 1, __name__)
    try:
        WebDriverWait(browser, 10).until(ec.presence_of_element_located(
            (By.ID, login_id)))
    except TimeoutException:
        adbot_utils.print_log("Failed to get login form", 0, __name__)
    else:
        adbot_utils.print_log("Logging in...", 1, __name__)

# uses to fill the log in form
def website_login(browser):
    get_login_form(browser)
    input_login = browser.find_element_by_id(login_id)
    input_passwd = browser.find_element_by_id(password_id)
    input_login.clear()
    input_passwd.clear()
    input_login.send_keys(login)
    input_passwd.send_keys(password)
    input_passwd.send_keys(Keys.RETURN)

# post the ad
def post(browser):
    browser.find_element_by_id("newadSubmit").click()
    # validate_ad(browser)

    return True

# fill the form to create an ad
def fill_form(browser, ad):
    input_title = browser.find_element_by_id("subject")
    input_description = browser.find_element_by_id("body")
    input_price = browser.find_element_by_id("price")
    input_address = browser.find_element_by_id("location_p")
    input_reference = browser.find_element_by_id("custom_ref")
    input_phone = browser.find_element_by_id("phone")
    browser.find_element_by_id("address").clear()
    input_title.clear()
    input_description.clear()
    input_price.clear()
    input_address.clear()
    input_phone.clear()
    input_title.send_keys(ad[0])
    input_description.send_keys(ad[1])
    input_price.send_keys(repr(int(ad[2])))
    input_phone.send_keys("0643095523")
    input_address.send_keys(ad[3])
    WebDriverWait(browser, 5).until(ec.presence_of_element_located(
        (By.XPATH, "/html/body/section[1]/main/section/section/form/div[1]/section[2]/article/div/div/div[1]/div[1]/div/ul/li")))
    browser.find_element_by_xpath(
        "/html/body/section[1]/main/section/section/form/div[1]/section[2]/article/div/div/div[1]/div[1]/div/ul/li").click()
    # pour choisir la categorie
    browser.find_element_by_id("cat34").click()

# upload images to create the ad
def upload_images(browser, cwd, ad):
    if not adbot_utils.get_page(browser, "", By.ID, "image0"):
        return False
    browser.find_element_by_id("image0").send_keys(cwd + "/resources/img/" + "nobo_11.jpg")
    WebDriverWait(browser, 50).until(ec.presence_of_element_located(
        (By.XPATH, "/html/body/section[1]/main/section/section/form/div[1]/section[1]/article/div[3]/section/aside/div[1]/img")))
    if not adbot_utils.get_page(browser, "", By.ID, "image1"):
        return False
    browser.find_element_by_id("image1").send_keys(cwd + "/resources/img/nobo_12.jpg" )
    WebDriverWait(browser, 50).until(ec.presence_of_element_located(
        (By.XPATH, "/html/body/section[1]/main/section/section/form/div[1]/section[1]/article/div[3]/section/aside/div[2]/img")))
    if not adbot_utils.get_page(browser, "", By.ID, "image2"):
        return False
    browser.find_element_by_id("image2").send_keys(cwd + "/resources/img/nobo_13.jpg")
    WebDriverWait(browser, 50).until(ec.presence_of_element_located(
        (By.XPATH, "/html/body/section[1]/main/section/section/form/div[1]/section[1]/article/div[3]/section/aside/div[3]/img")))
    return True

# uses after fill the ad's form to confirm that you want to post the ad
def validate_ad(browser):
    adbot_utils.print_log("Validating ad", 1, __name__)
    try:
        WebDriverWait(browser, 10).until(ec.presence_of_element_located(
            (By.ID, "accept_rule")))
    except TimeoutException:
        adbot_utils.print_log("Failed to validate ad", 0, __name__)
        browser.find_element_by_id("newadSubmit").click()
        validate_ad(browser)
    else:
        adbot_utils.print_log("Ad validated", 1, __name__)
        browser.find_element_by_id("accept_rule").click()
        if not adbot_utils.get_page(browser, "", By.ID, "lbc_submit"):
            adbot_utils.print_log("Failed to validate ad", 0, __name__)
        browser.find_element_by_id("lbc_submit").click()
        adbot_utils.print_log("Ad submited", 1, __name__)

def delete_old_ads(browser):
    website_login(browser)
    adbot_utils.print_log("Deleting ads", 1, __name__)
    try:
        WebDriverWait(browser, 10).until(ec.presence_of_element_located(
            (By.ID, "newadSubmit")))
    except TimeoutException:
        print("\nRien a supprimer")
        return
    else:
        browser.find_element_by_id("allChecked_top").click()
        browser.find_element_by_xpath(
            "/html/body/div/div/div[3]/div/div[1]/form[1]/div[1]/div[2]/a[2]").click()
        WebDriverWait(browser, 10).until(ec.presence_of_element_located(
            (By.ID, "adaction_confirm")))
        browser.find_element_by_css_selector('input.button-blue').click()
        time.sleep(2)
        adbot_utils.print_log("Old ads deleted", 1, __name__)
