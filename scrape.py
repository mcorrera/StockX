import bs4 as BeautifulSoup
import settings
import files
import selensetup
#import scripts
import prep


def processmainpage(url):
    inner = "css-1x3b5qq"
    outer = "product-tile css-1iewwf2-TileWrapper"

    html = prep.getpage(url)
    soup = prep.makesoup(html)
    numnewitems = 0
    for item in soup.find_all(class_=outer):
        new_item = settings.StockxItem()
        new_item.url = "https://stockx.com" + item.find('a')['href']
        new_item.name = item.find(class_=inner).text
        numnewitems += 1
        settings.Items.append(new_item)
    return numnewitems


def getitembidaskpage(url):
    html = prep.getpage(url)
    soup = prep.makesoup(html)
    if prep.checkpage(soup):
        selensetup.scrollwindow()

        selensetup.scrollwindow()

        bidaskclass = "chakra-stat__number css-1brf3jx"
        descptionclass = "chakra-text css-1h7lzbl"
        retailclass = "chakra-text css-1t6bihi"
        salesclass = "chakra-stat__number css-jcr674"
        salesclass2 = "chakra-stat__number.css-jcr674"
#        salesclass = "css-1e7tixd"

        bac = soup.find_all(class_=bidaskclass)
        rc = soup.find_all(class_=retailclass)
        dc = soup.find_all(class_=descptionclass)

        if selensetup.waitforit(salesclass2):
            soup = prep.remakesoup()
            sc = soup.find_all(class_=salesclass)
            sales = sc[3].text
        else:
            sales = ""
            error = True

        if len(bac) != 0:
            bid = bac[1].text
            ask = bac[0].text
            retail = ""
            for index, x in enumerate(rc):
                if x.text == "Retail":
                    retail = dc[index].text
            return True, bid, ask, sales, retail
        else:
            print("No Data Found")

            driver = selensetup.initucdriver()
            settings.init(driver)
            return False, "", "", "", ""
    else:
        print("No Data Found")
        selensetup.end()
        driver = selensetup.initucdriver()
        settings.init(driver)
        return False, "", "", "", ""


def compare():
    for index, item in enumerate(settings.Items):
        ok, currentbid, currentask, currentsales, retail = getitembidaskpage(item.url)
        if ok:
            if currentsales != item.sales:
                print(f"Sales Changed from {item.sales} to {currentsales} on {item.name}")
                item.sales = currentsales
            if currentbid != item.bid:
                print(f"Bid Changed from {item.bid} to {currentbid} on {item.name}")
                item.bid = currentbid
            if currentask != item.ask:
                print(f"Ask Changed from {item.ask} to {currentask} on {item.name}")
                item.ask = currentask
        if index % 20 == 0:
            files.writeitems()
            print(f"{index} Saved.")


def scrapemain(url, numpages):
    for i in range(1, numpages + 1):
        print(f"Getting page {i} of {numpages}")
        numberscrapped = processmainpage(url + str(i))
        print(f"{numberscrapped} Items scrapped. {len(settings.Items)} Total")
