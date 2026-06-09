import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []
for page in range(1, 4): # 3 pages = 60 books
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = float(book.find('p', class_='price_color').text[1:])
        rating = book.p['class'][1] # One, Two, Three, Four, Five
        books.append([title, price, rating])

df = pd.DataFrame(books, columns=['Title', 'Price', 'Rating'])
df.to_csv('books_data.csv', index=False)
print("✅ Task 1 Done! books_data.csv ready. Total:", len(df))