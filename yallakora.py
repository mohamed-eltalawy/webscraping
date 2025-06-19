import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("https://www.yallakora.com/match-center?date=10/3/2023#days")

def main(page):
    scr = page.content
    soup = BeautifulSoup(scr, "lxml")
    match_details = []

    championships = soup.find_all("div", {"class": "matchCard"})

    def get_matches_info(championship):
        championship_title = championship.contents[1].find("h2").text.strip()
        matches = championship.contents[3].find_all("div", {"class": "liItem"})
        for i in range(len(matches)):
            teamA = matches[i].find("div", {"class": "teamA"}).text.strip()
            teamB = matches[i].find("div", {"class": "teamB"}).text.strip()
            result_of_match = matches[i].find("div", {"class": "MResult"}).find_all("span", {"class": "score"})
            score = f"{result_of_match[0].text.strip()} : {result_of_match[1].text.strip()}"
            match_time = matches[i].find("div", {"class": "MResult"}).find("span", {"class": "time"}).text.strip()

            match_details.append({
                "نوع البطولة": championship_title,
                "الفريق الاول": teamA,
                "الفريق الثاني": teamB,
                "ميعاد المباراة": match_time,
                "النتيجة": score
            })

    for i in range(len(championships)):
        get_matches_info(championships[i])

    if match_details:
        keys = match_details[0].keys()
        with open("D:\BA\py\matches.csv", "w", newline='', encoding="utf-8-sig"   ) as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(match_details)
            print("✅ File created: matches.csv")
    else:
        print("⚠️ No match data found.")

main(page)

