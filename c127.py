import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver 
import requests

brighteststars= "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(brighteststars)
#browser = webdriver.Edge(r"C:\Users\Sylvia 2\OneDrive\Desktop\proj127\msedgedriver.exe")
#browser.get(brighteststars)

scrape_data = []

def scrape():
    soup = BeautifulSoup(page.text, "html.parser")
    star_table = soup.find("table",attrs = {"class","wikitable"})
    tablebody = star_table.find("tbody")
    tablerows = tablebody.find_all("tr")

    for row in tablerows:
        tablecol = row.find_all("td")
        temp_list = []
        for col in tablecol:
            data = col.text.strip()
            temp_list.append(data)
        scrape_data.append(temp_list)
scrape()

stars_data = []

for i in range(1,len(scrape_data)):
    starname = scrape_data[i][1]
    stardist = scrape_data[i][3]
    starmass = scrape_data[i][5]
    starradius = scrape_data[i][6]
    starlum = scrape_data[i][7]
    req_data = [starname,stardist,starmass,starradius,starlum]
    stars_data.append(req_data)

headers = ["name","distance","mass","radius","luminosity"]
df = pd.DataFrame(stars_data,columns = headers)

print(df)

df.to_csv("proj127.csv",index = True,index_label = "ID")