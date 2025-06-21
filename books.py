import requests
from bs4 import BeautifulSoup
import pandas as pd
book_items=[]

for i in range (1,51):
    print(i)
    url=f"http://books.toscrape.com/catalogue/page-{i}.html"

    page=requests.get(url)

    scr=page.content

    soup=BeautifulSoup(scr,'lxml')

    books=soup.find_all("li",{'class':"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    
    for book in books:
        title=book.find("h3").text.strip()
        rating=book.find("p").text.strip()
        price=book.find("p",{'class':"price_color"}).text.strip()
        avilability=book.find("p",{"class":"instock availability"}).text.strip()

        books_list={
            "title":title,
            "rating":rating,
            'price':price,
            'avilability':avilability
        }
        book_items.append(books_list)

df=pd.DataFrame(book_items)

df.to_csv("book_store.csv",encoding="utf-8-sig",index=False)