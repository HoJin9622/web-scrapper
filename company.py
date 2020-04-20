import requests
from bs4 import BeautifulSoup

def get_name_url():
  alba_url = "http://www.alba.co.kr"

  company_url = []
  company_name = []

  result = requests.get(alba_url)
  soup = BeautifulSoup(result.text, "html.parser")
  information = soup.find("div", {"id":"MainSuperBrand"})
  market = information.find("ul", {"class":"goodsBox"})
  one_market = market.find_all("li", {"class":"impact"})

  for i in one_market:
    company_url.append(i.find("a")["href"])
    company_name.append(i.find("span", {"class":"company"}).string)

  return company_url, company_name
  
