import os
from tkinter import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


LOG_OK = Bcolors.OKBLUE + "[" + Bcolors.OKGREEN + "OK" + Bcolors.OKBLUE + "]" + Bcolors.ENDC
LOG_KO = Bcolors.OKBLUE + "[" + Bcolors.FAIL + "KO" + Bcolors.OKBLUE + "]" + Bcolors.ENDC

def print_log(log_text, is_ok, module_name):
    module_name = Bcolors.OKBLUE + "[" + Bcolors.OKGREEN + module_name + Bcolors.OKBLUE + "]" + Bcolors.ENDC
    if is_ok == 1:
        prefix = LOG_OK
    else:
        prefix = LOG_KO
        log_text = Bcolors.FAIL + log_text + Bcolors.ENDC
    # print(prefix, module_name, log_text)
    print(log_text)
    # T.insert(END, "\n" + log_text)
    # T.pack(side=TOP)
    # fenetre.update()


def get_page(browser, url, by_method, element_path):
    if url:
        browser.get(url)
    try:
        WebDriverWait(browser, 10).until(ec.presence_of_element_located((by_method, element_path)))
    except TimeoutException:
        if url:
            print_log("Failed to load page " + url, 0, __name__)
        else:
            print_log("Failed to load element [" + element_path + "]", 0, __name__)
        return False
    return True


def get_ads(ads_directory, ad_name):
    directory = os.fsencode(ads_directory)
    ads_xml = []
    if not directory:
        print_log("Invalid ad directory : " + ads_directory, 0, __name__)
        return None
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.startswith(ad_name):
            print_log("Ad [" + filename + "] matching ad name [" + ad_name + "]", 1, __name__)
            ads_xml.append(etree.parse(ads_directory + "/" + filename))
    return ads_xml
