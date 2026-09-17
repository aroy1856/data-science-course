import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import csv

url = "http://books.toscrape.com/"

response = requests.get(url)
response.encoding = "utf-8"

# Fetch webpage data
soup = BeautifulSoup(response.text, "html.parser")

# Extract product title, price, and image URL
titles = soup.find_all("h3")
prices = soup.find_all("p", class_="price_color")
images = soup.select("article.product_pod img")
for title, price, image in zip(titles, prices, images):
    print(title.text, price.text, urljoin(url, image.get("src")))

# Download product image
for image in images:
    image_url = urljoin(url, image.get("src"))
    image_response = requests.get(image_url)
    # write the image to a file in the images folder
    os.makedirs("images", exist_ok=True)
    with open(os.path.join("images", image_url.split("/")[-1]), "wb") as f:
        f.write(image_response.content)

# Compare product price with a target price
target_price = 100
for price in prices:
    amount = float(price.text.replace("£", "").replace("Â", ""))
    if amount < target_price:
        print(price.text)

# Handle multiple product URLs
product_links = soup.select("article.product_pod h3 a")
for link in product_links:
    product_url = urljoin(url, link.get("href"))
    product_response = requests.get(product_url)
    product_response.encoding = "utf-8"
    product_soup = BeautifulSoup(product_response.text, "html.parser")
    product_title = product_soup.find("h1")
    product_price = product_soup.find("p", class_="price_color")
    product_image = product_soup.select_one("#product_gallery img")
    if product_title and product_price and product_image:
        print(product_title.text, product_price.text, urljoin(product_url, product_image.get("src")))
        print("--------------------------------")

# write the product title, price, and image URL to a csv file
with open("products.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Image URL"])
    for title, price, image in zip(titles, prices, images):
        writer.writerow([title.text, price.text, urljoin(url, image.get("src"))])
