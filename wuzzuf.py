import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("https://wuzzuf.net/search/jobs/?q=illustrator&a=navbl")
scr=page.content
soup=BeautifulSoup(scr,"lxml")



containers=soup.find_all("div",{"class":"css-1gatmva e1v1l3u10"})

#creating csv file
with open(r"D:\BA\py\wuzzuf.csv", "w", encoding="utf-8")  as f:
    writer = csv.writer(f)
    writer.writerow(["job_title", "company_name", "company_location", "job_type", "experience_level"])

        #header="job_title,company_name,company_location,job_type,excperince_level"
        #f.write(header+"\n")



    for container in containers: 
        # Data Needed
        job_title=container.find("h2",{"class":"css-m604qf"}).text.strip()

        company_name=container.find("a",{"class":"css-17s97q8"}).text.strip()

        company_location=container.find("span",{"class":"css-5wys0k"}).text.strip()
        # job_details
        job_details=container.find("div",{"class":"css-y4udm8"})

        job_type=job_details.find("span",{"class":"css-1ve4b75"}).text.strip()

        excperience_level=job_details.find("a",{"class":"css-o171kl"}).text.strip()

        writer.writerow([job_title, company_name, company_location, job_type, excperience_level])

            #f.write(job_title + ", " + company_name+", "+company_location+", "+job_type+", "+excperince_level+ "\n")
            #excperince_level_inyears=job_details.find("span","css-o171kl").text.strip()
            #print(job_title ,company_name,company_location,job_type,excperince_level)
print("✅ File created: wuzuuf.csv")