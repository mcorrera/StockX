import csv
import settings


def writeitems():
    print(f"Writing {len(settings.Items)} Items")
    with open('gucci.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for index, item in enumerate(settings.Items):
            datastring = [item.name, item.bid, item.ask, item.sales, item.retail, item.url]
            writer.writerow(datastring)


def readitems():
    settings.Items = []
    with open('gucci.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            item = settings.StockxItem()
            item.name = row[0]


            item.bid = row[1]
            item.ask = row[2]
            item.sales = row[3]
            item.retail = row[4]
            item.url = row[5]
            settings.Items.append(item)
        print(f"Reading {len(settings.Items)} Items")
    return len(settings.Items)


def printitems():
    for index, item in enumerate(settings.Items):
        print(f"'{item.name}','{item.bid}','{item.ask},'{item.retail}','{item.url}'")
