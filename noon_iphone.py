from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import pandas as pd

header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"

}
service=Service(executable_path="D:\BA\py\edge driver\edgedriver_win64\msedgedriver.exe")

driver=webdriver.Edge(service=service)

url="https://www.noon.com/egypt-en/electronics-and-mobiles/mobiles-and-accessories/mobiles-20905/apple/"

driver.get(url)

mobile_list=[]

products=driver.find_elements(By.CLASS_NAME,"ProductBoxLinkHandler_linkWrapper__b0qZ9")

for product in products:
    iphone_name=product.find_element(By.CLASS_NAME,"ProductDetailsSection_title__JorAV").text
    rating=product.find_element(By.CLASS_NAME,"RatingPreviewStar_textCtr__sfsJG").text
    price=product.find_element(By.CLASS_NAME,"Price_amount__2sXa7").text

    list_item={
        "iphone_name":iphone_name,
        "rating":rating,
        "price":price
    }
    mobile_list.append(list_item)

df=pd.DataFrame(mobile_list)

df.to_csv("noon_iphone.csv",encoding="utf-8-sig",index=False)