from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs#Field_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(10)

scr_dwarf_data=[]

def scrape():
    soup=BeautifulSoup(browser.page_source,"html.parser")
    brown_dwarf_table=soup.find("table", attrs={"class","wikitable sortable jquery-tablesorter"})
   #brown_dwarf_table=brown_dwarf_table1[2]
    t_body=brown_dwarf_table.find('tbody')
    t_rows=brown_dwarf_table.find_all('tr')

    for row in t_rows:
        t_col=row.find_all('td')
        temp_list=[]
        for col_data in t_col:
            data=col_data.text.strip()
            temp_list.append(data)
        scr_dwarf_data.append(temp_list)

#calling function
scrape()
dwarf_data=[]

for i in range(1,len(scr_dwarf_data)):
    name=scr_dwarf_data[i][0]
    cons=scr_dwarf_data[i][1]
    dec=scr_dwarf_data[i][3]
    dis=scr_dwarf_data[i][5]
    mass=scr_dwarf_data[i][6]
    rad=scr_dwarf_data[i][7]

    req_data=[name,cons,dec,dis,mass,rad]
    dwarf_data.append(req_data)

print(dwarf_data)
headers=[
'Brown dwarf'	,'Constellation'	,'Declination','Distance (ly)'	
,'Mass (MJ)','Radius (RJ)']

# Define pandas DataFrame   
Dward_df = pd.DataFrame(dwarf_data, columns=headers)

#Convert to CSV
Dward_df.to_csv('dwarf_scra_data.csv',index=True, index_label="id")