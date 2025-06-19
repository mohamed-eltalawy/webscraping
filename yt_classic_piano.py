import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

service=Service(executable_path="D:\downlaods\driver\edgedriver_win64\msedgedriver.exe")

driver=webdriver.Edge(service=service)

url="https://www.youtube.com/@EssentialClassics/videos"

driver.get(url)

time.sleep(10)


videos=driver.find_elements(By.TAG_NAME,'ytd-rich-item-renderer')

#//*[@id="video-title"]

#//*[@id="overlays"]/ytd-thumbnail-overlay-time-status-renderer/div[1]/badge-shape/div

#//*[@id="metadata-line"]/span[1]

#//*[@id="metadata-line"]/span[2]
vid_list=[]
for video in videos:
    title=video.find_element(By.XPATH,'.//*[@id="video-title"]').text
    duration=video.find_element(By.XPATH,'.//*[@id="overlays"]//ytd-thumbnail-overlay-time-status-renderer').text
    views=video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[1]').text
    since=video.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[2]').text

    vid_item={
        "title":title,
        "duration":duration,
        "views":views,
        "posted":since
    }
    vid_list.append(vid_item)

df=pd.DataFrame(vid_list)

df.to_csv("classic_piano.csv",encoding="utf-8-sig",index=False)