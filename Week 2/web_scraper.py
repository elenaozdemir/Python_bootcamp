import requests   #module to make http / https requests
import html5lib
from bs4 import BeautifulSoup

amazon_url = "https://www.amazon.com/dp/B07YNHPFNB/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B07YNHPFNB&pd_rd_w=1mrK1&pf_rd_p=45a72588-80f7-4414-9851-786f6c16d42b&pd_rd_wg=DM3GM&pf_rd_r=P5ECBFPVZCJYBPH2YP76&pd_rd_r=53c9f21a-f8a4-4edf-bb5b-c699e3edecce&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExWTFPQkc3MEVFVU9GJmVuY3J5cHRlZElkPUEwMjcyNDIzR05OVUhCRUNQVFcxJmVuY3J5cHRlZEFkSWQ9QTAzMTM2MzlXN0o5OFI0TTlYMDkmd2lkZ2V0TmFtZT1zcF9kZXRhaWwmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"

agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"

# making a dictionary

agent_header = {
    "User-Agent.": agent
}
# use request library to get something: what you are trying to get, identify yourself
amazon_page = requests.get(amazon_url, headers=agent_header)

soup = BeautifulSoup(amazon_page.content, "html5lib")

# search for a specific ID in the soup
price_span = str(soup.find(id="priceblock_ourprice"))
print(price_span)

price = ''
for char in price_span:
    # will check if it a digit (0-9): only concerned about digits & decimals
    # will put at the end of a string
    if char.isdigit() is True:
        price += char
    if char == ".":
        price += char

# print(price)
price = float(price)
max_price = 1000

# will compare prices
if price <= max_price:
    print("You can buy it now!")
else:
    print("Can't afford it, make more money")