import os
import csv
import requests
from bs4 import BeautifulSoup
from company import get_name_url

os.system("clear")

company_url = []
company_name = []

[company_url, company_name] = get_name_url()

for i in range(len(company_url)):
  result = requests.get(company_url[i])
  soup = BeautifulSoup(result.text, "html.parser")
  recruit_information = soup.find("div", {"id":"NormalInfo"})
  markets = recruit_information.find("tbody")
  all_markets = markets.find_all("tr",{"class":""})

  print("place, title, time, pay, date")
  file = open(f"{company_name[i]}.csv", mode="w") 
  writer = csv.writer(file)
  writer.writerow(["place", "title", "time", "pay", "date"])
  for market in all_markets:

    try:
      place = market.find("td", {"class":"local first"}).get_text()
      title = market.find("td", {"class":"title"}).find("span",{"class":"company"}).get_text(strip=True)
      time = market.find("td",{"class":"data"}).get_text()
      pay = market.find("td",{"class":"pay"}).get_text()
      date = market.find("td", {"class":"regDate last"}).get_text()
      print(f"{place}, {title}, {time}, {pay}, {date}")

      writer.writerow([f"{place}", f"{title}", f"{time}", f"{pay}", f"{date}"])
    except:
      print("No")

