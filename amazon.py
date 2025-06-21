from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"}

services=Service(executable_path="D:\BA\py\edge driver\edgedriver_win64\msedgedriver.exe")

driver=webdriver.Edge(service=services)

url="https://www.amazon.eg/s?i=beauty&rh=n%3A21826043031%2Cp_n_availability%3A21909181031%2Cp_6%3AA30R10HFVEJ6ZE&s=popularity-rank&dc&fs=true&qid=1750549795&rnid=21909121031&ref=sr_nr_p_6_1&ds=v1%3Ac0PYPLkvHoP%2FLfQ8UhLLfw3BM5YRHX5aAyYNUanXQp8"

driver.get(url)
list_items=[]
WebDriverWait(driver, 15)

items=driver.find_elements(By.CSS_SELECTOR,"div[data-asin][data-component-type='s-search-result']")

for item in items:
    try:
        product_name=item.find_element(By.CSS_SELECTOR,"div[data-cy='title-recipe']").text
    except:
        product_name="N/A"
     
    try:
        price=item.find_element(By.CLASS_NAME,"a-price-whole").text
    except:
        try:
            price=item.find_element(By.CSS_SELECTOR,"div[data-cy='secondary-offer-recipe']").text
        except:
            price="N/A"    
    items_list={
        "product_name":product_name,
        "price":price
    }    
    list_items.append(items_list)

df=pd.DataFrame(list_items)

df.to_csv("products_perfuim_amazon.csv",encoding='utf-8-sig',index=False)
time.sleep(10)