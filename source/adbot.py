#!/usr/bin/python
# coding: utf-8

import adbot_utils
import extract_excel
import os
from tkinter import *
from websites_ads import leboncoin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random


cwd = os.getcwd()

# fenetre = Tk()
# label = Label(fenetre, text="Adbot Leboncoin post")
# label.pack()
# T = Text(fenetre, width=100, height=100, bg='ivory')
# label1 = Label(fenetre, text="COMPTE: " + leboncoin.login)
# label1.pack()
# label2 = Label(fenetre, text="PASSWORD: " + leboncoin.password)
# label2.pack()

def makeSomething():
    leboncoin.login = "123@123.fr"
    leboncoin.password = "1234567890"
    # T.insert(END, "\n" + "COMPTE: " + leboncoin.login )
    # T.insert(END, "\n" + "PASSWORD: " + leboncoin.password )
    label1.config(text="COMPTE: " + leboncoin.login)
    label2.config(text="PASSWORD: " + leboncoin.password)
    fenetre.update_idletasks()
    fenetre.update()

def headless_chromium():
    options = webdriver.ChromeOptions()
    options.binary_location = chromium_path
    options.add_argument('headless')
    options.add_argument('window-size=1024x900')
    return webdriver.Chrome(chrome_options=options)

# def print_in_console_log(T, fenetre, message):
#     T.insert(END, message)
#     T.pack(side=TOP)
#     fenetre.update()

def obtain_range(filename):
    stock = []
    f=open(filename)
    lines=f.readlines()
    stock = [int(lines[0]), int(lines[1])]
    return stock

def set_range(filename, begin, end, size):
    with open(filename, "r") as file:
        lines = file.readlines()
    lines[0] = str(end + 1) + "\n"
    if (end + 40) > size:
        lines[1] = str(size) + "\n"
    else:
        lines[1] = str(end + 40) + "\n"
    with open(filename, "w") as file:
        for line in lines:
            file.write(line)

def main_ad():
    print("OOOOOOOpass1")
    ads = extract_excel.ads_from_excel()
    print("pass2")
    size_ads = len(ads)
    print("pass3")
    stock = obtain_range("range.txt")
    print("pass4")
    range_begin = stock[0]
    range_end = stock[1]
    # browser = webdriver.Chrome()
    print("pass5")
    browser = webdriver.PhantomJS()
    adbot_utils.print_log("Browser loaded", 1, __name__ )
    browser.set_window_size(1024, 900)
    browser.implicitly_wait(10)
    leboncoin.post_ad(browser, range_begin, range_end, ads)
    adbot_utils.print_log("Program finished", 1, __name__)
    set_range("range.txt", range_begin, range_end, size_ads)
    print("finish")
    browser.quit()

def main_delete():
    browser = webdriver.Chrome()
    adbot_utils.print_log("Browser loaded", 1, __name__)
    browser.set_window_size(1024, 900)
    browser.implicitly_wait(10)
    leboncoin.delete_old_ads(browser, T, fenetre)
    adbot_utils.print_log("Program finished", 1, __name__)
    browser.quit()

# Button(fenetre, text ='CREATE ADS', command=main_ad).pack(side=TOP, padx=5, pady=5)
# Button(fenetre, text ='DELETE ADS', command=main_delete).pack(side=TOP, padx=5, pady=5)
# Button(fenetre, text ='change compte', command=makeSomething).pack(side=TOP, padx=5, pady=5)
#
# T.pack(side=TOP)
# T.insert(END, "Just a text Widget in two lines ")
# fenetre.mainloop()
# main_delete()
main_ad()
# print("finish")
