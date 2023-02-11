import scripts
import bidscripts
import selensetup
import settings
import files
import time
import scrape

if __name__ == '__main__':
    print("Hello")
    driver = selensetup.initucdriver()
    settings.init(driver)
    scripts.login()
    if settings.loggedin:
        settings.Bids = []
        #bidscripts.getbids()
        bidscripts.readbids()
        bidscripts.showbids()
        bidscripts.adjustbids()
        #bidscripts.writebids()

    time.sleep(45)
    settings.end()

# bidscripts.readbids()
# bidscripts.checkbids()