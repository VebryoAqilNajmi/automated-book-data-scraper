import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

# looping page 1 sampai 50
for page in range(1, 51):

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        # title
        title = book.h3.a["title"]

        # price
        price = book.find("p", class_="price_color").text
        price = float(price.replace("Â£", "").replace("£", ""))

        # stock
        stock = book.find("p", class_="instock availability").text.strip()

        # rating
        rating = book.find("p")["class"][1]

        data.append({
            "Title": title,
            "Price": price,
            "Stock": stock,
            "Rating": rating
        })

    print(f"Page {page} berhasil di-scrape")

# dataframe
df = pd.DataFrame(data)

# export csv
df.to_csv("books_data.csv", index=False)

print("=================================")
print("Semua data berhasil disimpan!")
print(f"Total data: {len(df)}")