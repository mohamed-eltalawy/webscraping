from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

url = "https://www.youtube.com/@JohnWatsonRooney/videos"

service = Service(executable_path="D:/downlaods/driver/edgedriver_win64/msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get(url)

# استنى الصفحة تحمل المحتوى
time.sleep(5)

# استهدف عناصر الفيديو الحقيقي (وليس عناصر شكلية)
videos = driver.find_elements(By.TAG_NAME, "ytd-rich-item-renderer")

for video in videos:
    try:
        title = video.find_element(By.ID, "video-title").text
        views = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text
        posted = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[2]').text
        print(f"Title: {title}")
        print(f"Views: {views}")
        print(f"Posted: {posted}")
        print("=" * 50)
    except Exception as e:
        print(f"Error: {e}")

driver.quit()
