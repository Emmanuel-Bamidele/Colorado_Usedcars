from bs4 import BeautifulSoup as sp
from urllib.request import urlopen as uReq
import json

my_url = "https://offerup.com/explore/k/cars-trucks/"

# opening connection and grabbing page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parser
page_soup = sp(page_html, "html.parser")
# grab each product
containers = page_soup.findAll("div", {"class": "_b31be13"})

filename = "colorado_car.csv"
f = open(filename, "w")

#head = "New_Listing", "Item_Price\n"

# f.write(head)

for container in containers:
    car_listing = container.findAll("div", {"class": "_1g9xn5a"})
    Listing = car_listing[0].span.text

    car_price = container.findAll("div", {"class": "_1ndiotn"})
    Price = car_price[0].text

    print("New List: " + Listing)
    print("Price: " + Price)
    print("Page Link: " + my_url)

    f.write(Listing.replace(",", " ") + "," +
            Price.replace(",", " ") + "\n")

f.close()
