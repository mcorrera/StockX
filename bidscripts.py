import time
import csv
from selenium.webdriver.common.by import By

import selensetup
import settings
import prep


def getbids():
    print("Getting Bids")
    global Bids
    time.sleep(15)
    url = "https://stockx.com/buying"
    html = prep.getpage(url)
    soup = prep.makesoup(html)
    if prep.checkpage(soup):
        rowclass = "css-y33p0s"
        selensetup.waitforit(rowclass)

        rc = soup.find_all(class_=rowclass)
        if len(rc) != 0:
            for row in rc:
                infoclass = "css-1uyy51i"
                ic = row.find_all(class_=infoclass)
                if len(ic) != 0:
                    newbid = settings.ItemBid();
                    newbid.name = ic[0].text
                    #int(row[1].replace("$", ""))
                    newbid.currentbid = int(ic[1].text.replace("$",""))
                    newbid.highbid = int(ic[2].text.replace("$",""))
                    newbid.lowask = ic[3].text
                    newbid.expires = ic[4].text
                    newbid.edit = "https://stockx.com" + ic[5].find('a')['href']
                    settings.Bids.append(newbid)
    else:
        print("Checkpage Failed")
        selensetup.resetdriver()
        getbids()



def increasebid(bid):
    newbid = bid.currentbid + 1
    print(f"Increasing Bid on {bid.name} from {bid.currentbid} to {newbid}. Max is {bid.maxbid}")
    url = bid.edit
    html = prep.getpage(url)
    soup = prep.makesoup(html)
    mybutton = ".css-32hjx7"
    if prep.checkpage(soup):
        selensetup.waitforit(mybutton)
        settings.driver.find_element(By.CSS_SELECTOR, mybutton).click()
        time.sleep(.5)
        settings.driver.find_element(By.NAME, "ask-amount").clear()
        settings.driver.find_element(By.NAME, "ask-amount").send_keys(newbid)
        #settings.driver.find_element(By.CSS_SELECTOR, ".css-1g5iawp").click()
        time.sleep(.5)
        #settings.driver.find_element(By.CSS_SELECTOR, ".css-1g5iawp").click()
        bid.currentbid = newbid
        print("Bid Increased")


def adjustbids():
    for bid in settings.Bids:
        if bid.currentbid < bid.highbid:
            if bid.currentbid < bid.maxbid:
                increasebid(bid)



def showbids():
    for bid in settings.Bids:
        print(f"Item = {bid.name} Current Bid = {bid.currentbid} Max Bid = {bid.maxbid}  High Bid = {bid.highbid} Low Ask = {bid.lowask} Expires = {bid.expires} Edit = {bid.edit}")


def writebids():
    print(f"Writing {len(settings.Bids)} Bids")
    with open('bids.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for index, bid in enumerate(settings.Bids):
            datastring = [bid.name, bid.currentbid, bid.maxbid, bid.highbid, bid.expires, bid.edit]
            writer.writerow(datastring)


def readbids():
    settings.Bids = []
    with open('bids.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            bid = settings.ItemBid()
            bid.name = row[0]
            bid.currentbid = int(row[1].replace("$",""))
            bid.maxbid = int(row[2].replace("$",""))
            bid.highbid = int(row[3].replace("$",""))
            #bid.lowask = int(row[4].replace("$",""))
            bid.expires = row[4]
            bid.edit = row[5]
            settings.Bids.append(bid)
        print(f"Reading {len(settings.Bids)} Bids")
    return len(settings.Bids)
