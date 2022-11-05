import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver 
import requests

dwarfstars= "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(dwarfstars)

dwarf_scraped = []

def scrape2():
    soup = BeautifulSoup(page.text, "html.parser")
    star_table2 = soup.find_all("table")

    tablebody2 = star_table2[7].find("tbody")
    tablerows2 = tablebody2.find_all("tr")

    for xrows in tablerows2:
        xtablecol = xrows.find_all("td")
        temp_list = []
        for xcol in xtablecol:
            data2 = xcol.text.strip()
            temp_list.append(data2)
        dwarf_scraped.append(temp_list)
scrape2()

dwarf_stars_data = []

for light in range(1,len(dwarf_scraped)):
    dwarf_name = dwarf_scraped[light][0]
    dwarf_mass = dwarf_scraped[light][7]
    dwarf_radius = dwarf_scraped[light][8]
    dwarf_dist = dwarf_scraped[light][5]

    all_dwarf_data = [dwarf_name,dwarf_dist,dwarf_mass,dwarf_radius]
    dwarf_stars_data.append(all_dwarf_data)

    
headers = ["name","distance","mass","radius"]
df = pd.DataFrame(dwarf_stars_data,columns = headers)

df.to_csv("proj1287.csv",index = True,index_label = "ID")