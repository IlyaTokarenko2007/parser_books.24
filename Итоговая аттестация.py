from bs4 import BeautifulSoup
import requests
import csv

page = 1

url = 'https://book24.ru/'
html = requests.get(url).content

bs = BeautifulSoup(html, 'html.parser')
books_html = bs.find_all('article', class_='product-card _without-button')

with open('books.xml', 'w', encoding='utf-8') as file:
    for book in books_html:
        file.write(book.prettify())

books = []
for book in books_html:
    title = book.find('a', {'class': 'product-card__name'}).text.strip()
    author = book.find('div', {'class': 'author-list product-card__authors-holder'}).get_text()
    img = book.find('img', {'class': 'product-card__image'})['data-src']
    price = int(book['data-b24-price'])
    books.append({'title': title, 'author': author, 'img': img, 'price': price})


with open('books.csv', 'w', encoding='utf-8') as file:
    names = ['title', 'author', 'img', 'price']
    writer = csv.DictWriter(file, fieldnames=names)

    writer.writeheader()
    writer.writerows(books)
