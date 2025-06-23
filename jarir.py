from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"}


service=Service(executable_path="D:\BA\py\edge driver\edgedriver_win64\msedgedriver.exe")
driver=webdriver.Edge(service=service)
url="https://www.jarir.com/sa-en/apple.html"

driver.get(url)
# Scroll down to load all products (repeat scrolling to make sure all are loaded)
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  # Allow time for loading

    # Check if we've reached the bottom
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"product-tile")))

products=driver.find_elements(By.CLASS_NAME,"product-tile")
list_items=[]
for product in products:
    try:
        title= product.find_element(By.CLASS_NAME,"product-title__title").text
    except:
        title= ""
    try:    
        info=product.find_element(By.CLASS_NAME,"product-title__info").text
    except:
        info=""
    try:
        price=product.find_element(By.CLASS_NAME,"price").text
    except:
        price=""
    try:    
        save=product.find_element(By.CLASS_NAME,'notification__save').text
    except:
        save=""   
    items={
        "title":title,
        "info":info,
        "price":price,
        "save":save
    }

    list_items.append(items)
df=pd.DataFrame(list_items)
df.to_csv("jarir_phones.csv",encoding="utf-8-sig",index=False)