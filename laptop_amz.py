from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
import pandas as pd

# إعداد خيارات المتصفح
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0")
options.add_argument("accept-language=ar,en-US;q=0.9,en;q=0.8")


service=Service(executable_path=r"D:\BA\py\edge driver\edgedriver_win64\msedgedriver.exe")

driver=webdriver.Edge(service=service,options=options)

url="https://www.amazon.eg/s?k=Gaming+laptop&i=electronics&rh=n%3A18018102031%2Cp_123%3A308445%257C391242&dc&ds=v1%3Ai%2BLvhHLp8jiBSdJ%2BhvHYIp05oYARoTVm3hIL7nLz8Vo&_encoding=UTF8&pf_rd_p=637c9607-6c53-4664-941c-97826d452f6a&pf_rd_r=ZJRM1R6XA5AJYJESW65W&qid=1753624183&rnid=91049076031&ref=sr_nr_p_123_2"


driver.get(url)
time.sleep(5)
content=driver.find_elements(By.CLASS_NAME,"sg-col-inner")
list_item=[]
for item in content:
    try:
        desc=item.find_element(By.CSS_SELECTOR,"h2 span").text
    except:
        continue
    try:
        review = item.find_element(By.CSS_SELECTOR, "span.a-icon-alt").get_attribute("innerHTML")
    except:
        review = "غير متوفر"
    try:
        #num_reviews=item.find_element(By.CSS_SELECTOR,"span.total-review-count").get_attribute("innerHTML")
        num_reviews = item.find_element(By.CSS_SELECTOR, "div.a-row.a-size-small span.a-size-base.s-underline-text").text
    except:    
        num_reviews = "غير متوفر"
    try:
        price = item.find_element(By.CLASS_NAME, "a-price-whole").text
    except:
        continue
    
    items={
        'product_description':desc,
        'product_review':review,
        'number_reviwes':num_reviews,
        'price':price
    }
    list_item.append(items)

df=pd.DataFrame(list_item)
df.to_csv("amazon_laptop.csv",encoding="utf-8-sig",index=False)
