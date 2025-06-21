from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import pandas as pd
import csv

header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"

}
service=Service(executable_path="D:\BA\py\edge driver\edgedriver_win64\msedgedriver.exe")

driver=webdriver.Edge(service=service)

url="https://www.noon.com/egypt-en/iphone-16-pro-max-256gb-desert-titanium-5g-with-facetime-international-version/N70106183V/p/?o=e1042be15c90771b&shareId=90f19fce-ea74-4881-809d-5a2cd6789c08"

driver.get(url)

mobile_list=[]

products_specifications=driver.find_elements(By.CLASS_NAME,"SpecificationsTab_column__k2ADo")
with open("table_data_speci.csv",mode="w",encoding="utf-8-sig",newline="") as file:
    writer=csv.writer(file)
    for product in products_specifications:
        tables=product.find_elements(By.TAG_NAME,"table")
        for table in tables:
            table_body=table.find_element(By.TAG_NAME,"tbody")
            rows = table_body.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                columns = row.find_elements(By.TAG_NAME, "td")  # أو "th" لو عنوان عمود
                row_data = [col.text.strip() for col in columns]

                if row_data:  # لو الصف مش فاضي
                    writer.writerow(row_data)   # ✅ حفظ في CSV
                    print(row_data)             # ✅ عرض في الكونسول
                   
    
    