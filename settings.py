global Bids
global Items
global StockxItem
global driver
global loggedin


def init(webdriver):
    global driver
    global loggedin
    driver = webdriver
    loggedin = False


def zeroitems():
    global Items
    global Bids
    Items = []
    Bids = []


def end():
    global driver
    driver.quit()


class StockxItem:
    def __init__(self):
        self.brand = ""
        self.retail = ""
        self.name = ""
        self.url = ""
        self.bid = 0
        self.ask = 0
        self.sales = 0


class ItemBid:
    def __init__(self):
        self.name = ""
        self.url = ""
        self.currentbid = 0
        self.maxbid = 0
        self.minbid = 0
        self.lowask = 0
        self.expires = ""
        self.edit = ""
