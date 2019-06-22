from bs4 import BeautifulSoup as sp
from urllib.request import urlopen as uReq

my_url = "https://offerup.com/explore/k/cars-trucks/"

# opening connection and grabbing page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parser
page_soup = sp(page_html, "html.parser")
# grab each product
containers = page_soup.findAll("div", {"class": "_b31be13"})

filename = "colorado_cars.csv"
csv = open(filename, "w")

columTitleRow = "New List, Asking Price\n"
csv.write(columTitleRow)


for container in containers:
    car_listing = container.findAll("div", {"class": "_1g9xn5a"})
    Listing = car_listing[0].span.text

    car_price = container.findAll("div", {"class": "_1ndiotn"})
    Price = car_price[0].text

    print("New List: " + Listing)
    print("Price: " + Price + "\n")

    csv.write(Listing.replace(",", " ") + "," + Price.replace(",", " ") + "\n")

csv.write("These are the latest cars listed on Offerup for sale in Colorado, to purchase, visit Page Link: " + my_url)
