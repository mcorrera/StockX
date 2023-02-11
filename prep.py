import settings
import selensetup
from bs4 import BeautifulSoup
import scripts


def getpagesource ():
    html = settings.driver.page_source
    return html


def getpage(url):
    settings.driver.get(url)
    html = getpagesource()
    print("URL=",url)
    return html


def remakesoup():
    html = getpagesource()
    page = makesoup(html)
    return page


def makesoup(html):
    page = BeautifulSoup(html, 'lxml')
    return page


def findtext(soup, text):
    #    y = soup.find_all(text=text)
    if len(soup.find_all(text=text)) != 0:
        return True
    else:
        return False



def findelement(soup, element):
    y = soup.find_all(class_=element)
    if len(y) != 0:
        return True
    else:
        return False




def checkpage(soup):
    errortext = "Access denied"
    if findtext(soup, errortext):
        print("Access Denied")
        return False

    countrytext = "Choose Your Location"
    if findtext(soup, countrytext):
        print("Found Country")
        scripts.closecountry()
    else:
        print("Country Not Found")

    element = "chakra-modal__close-btn css-1qgkntd"
    if findelement(soup, element):
        print("Found Contest")
        scripts.closecontest()
    else:
        print("NOT Found Contest")

    return True
