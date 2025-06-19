from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

url="https://www.youtube.com/@JohnWatsonRooney/videos"

service=Service(executable_path="D:\downlaods\driver\edgedriver_win64\msedgedriver.exe")

driver=webdriver.Edge(service=service)

driver.get(url)
time.sleep(5)
videos=driver.find_elements(By.TAG_NAME,'ytd-rich-item-renderer')

videos_list=[]
for video in videos:
    title=video.find_element(By.ID,"video-title").text
    views=video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[1]').text
    when=video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[2]').text
    vid_item={
          "title":title,
          "views":views,
          "posted":when  
    }
    
    videos_list.append(vid_item)

df=pd.DataFrame(videos_list)

df.to_csv("videos_detals.csv",encoding="utf-8-sig", index=False)
driver.quit()