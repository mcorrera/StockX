from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import settings
import prep
import selensetup
import files


def getsales(url):
    html = prep.getpage(url)
    classname = "chakra-button.css-2yrtpe"  # Asks
    y = settings.driver.find_elements(By.CLASS_NAME, classname)
    print(y[2].text)
    y[2].click()
    # driver.execute_script("arguments[0].click();", y)
    print("clicked")
    selensetup.randomsleep()


def login():
    url = "https://stockx.com/login"
    html = prep.getpage(url)
    soup = prep.makesoup(html)
    username = "info@sandia.com"
    password = "Lindo123$"
    loginid = "nav-login"
    emailid = "email-login"
    #loginbuttonxpath = "//div[@id=\'header-wrapper\']/div/div/ul/li[5]/a"

    if prep.checkpage(soup):
        selensetup.waitforID(emailid)
        selensetup.scrollwindow()
        settings.driver.find_element(By.ID, emailid).send_keys(username)
        settings.driver.find_element(By.ID, "email-login").send_keys(username)
        time.sleep(.5)
        settings.driver.find_element(By.ID, "password-login").send_keys(password)
        selensetup.scrollwindow()

        settings.driver.find_element(By.ID, "btn-login").click()
        print("Logged In")
        settings.loggedin = True
    else:
        print("NOT Logged In")
        settings.loggedin = False



def closecookies():
    # getpage("https://www.stockx.com")
    settings.driver.find_element(By.CSS_SELECTOR, ".css-unzfas-button").click()


def closecountry():
    settings.driver.find_element(By.CSS_SELECTOR, ".chakra-modal__close-btn").click()


def closecontest():
    settings.driver.find_element(By.CSS_SELECTOR, ".chakra-modal__close-btn").click()



def getallsales():
    for index, item in enumerate(settings.Items):
        getsales(item.url)
        if index % 20 == 0:
            files.writeitems()
            print(f"{index} Saved.")
