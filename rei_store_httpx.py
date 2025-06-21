from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd



header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"

}
service=Service(executable_path="D:\BA\py\edge driver\edgedriver_win64\msedgedriver.exe")

driver=webdriver.Edge(service=service)

items_list=[]
for page in range(1,17):

    url=f"https://www.rei.com/c/tents?page={page}"

    driver.get(url)
    WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "VcGDfKKy_dvNbxUqm29K")))

    contents=driver.find_elements(By.CLASS_NAME,"VcGDfKKy_dvNbxUqm29K")
    
    #//*[@id="search-results"]/ul/li[1]/a[2]/span/span[1]
    #Qw6mvRoX0xm5QsSku4hy
    for content in contents:
        title=content.find_element(By.CLASS_NAME,'dBj29YaudGjV80UCeSh_').text
        price=content.find_element(By.XPATH,'.//span[contains(text(),"$")]').text
        product_details=content.find_elements(By.CLASS_NAME,"PbkM8qMJIiUeqTHrk9pC")
        #sleeping_capacity=product_details[0].find_element(By.CLASS_NAME,"Qw6mvRoX0xm5QsSku4hy").text
        #season=product_details[1].find_element(By.CLASS_NAME,"Qw6mvRoX0xm5QsSku4hy").text
        
        if len(product_details) > 0:
            try:
                sleeping_capacity = product_details[0].find_element(By.CLASS_NAME, "Qw6mvRoX0xm5QsSku4hy").text
            except:
                sleeping_capacity = "N/A"

# لو لقيت ثاني عنصر حاول تجيب منه الـ season
        if len(product_details) > 1:
            try:
                season = product_details[1].find_element(By.CLASS_NAME, "Qw6mvRoX0xm5QsSku4hy").text
            except:
                season = "N/A"


        list_item={
            "title":title
            ,"price":price,
            "sleeping_capacity":sleeping_capacity,
            "season":season
        }

        items_list.append(list_item)

df=pd.DataFrame(items_list)

df.to_csv("rie_store_selenium.csv",encoding="utf-8-sig",index=False)
