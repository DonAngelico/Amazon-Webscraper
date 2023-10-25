# Import libraries

import requests
import smtplib
import time
import datetime
import csv
from bs4 import BeautifulSoup


# Connect to Website and pull in data

def check_price():
    URL = 'https://www.amazon.com/iFixit-Repair-Business-Toolkit-Smartphone/dp/B0BXYBMGDY/ref=b2b_gw_d_ab_lists_widget_sccl_1/130-6746188-2099749?pd_rd_w=HR9dU&content-id=amzn1.sym.e1612812-dfc0-4992-8454-ce8b8c97ea8b&pf_rd_p=e1612812-dfc0-4992-8454-ce8b8c97ea8b&pf_rd_r=VA7NNK31ZTS68FTW1N3W&pd_rd_wg=fRic8&pd_rd_r=4799d71b-2c11-49d6-8c30-a46751300167&pd_rd_i=B0BXYBMGDY&psc=1'

    headers = {
    "User-Agent": "Enter your user agent info",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
}


    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(id='priceblock_ourprice').get_text()

# Clean up the data a little bit

    price = price.strip()[1:]
    title = title.strip()

# Create a Timestamp for your output to track when data was collected
    today = datetime.date.today()

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

# Create CSV and write headers and data into the file
    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

# Runs check_price after a set time and inputs data into your CSV
while True:
    check_price()
    time.sleep(60)  # Change the sleep interval if needed (e.g., 3600 for 1 hour)
