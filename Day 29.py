'''
day 29 of my python course
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

#Step 1: Web Scraping
url = "http://books.toscrape.com/"

try:
    response = requests.get(url)
    response.encoding = 'utf-8'        # Fix encoding issue
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
    exit()

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_ = "product_pod")

book_names = []
book_prices = []

for book in books:
    name = book.h3.a["title"]

    # Get raw price text
    price_text = book.find("p", class_ = "price_color").text

    # Extract numeric value using reqex (fix for AE issue)
    price = float(re.findall(r"\d+\.\d+", price_text)[0])

    book_names.append(name)
    book_prices.append(price)

df = pd.DataFrame({"Book_Name": book_names, "Price": book_prices})
print(df)
print(df.shape)
print(df.head())
df.to_csv("books_data.csv", index = False)
print("CSV File Saved Successfully!")
plt.figure(figsize = (10,5))
plt.bar(df["Book_Name"][:10], df["Price"][:10])
plt.xticks(rotation = 90)
plt.xlabel("Book Names")
plt.ylabel("Price(Rs)")
plt.title("Top 10 Book Prices")
plt.tight_layout()
plt.show()
