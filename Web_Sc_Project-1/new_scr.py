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

dwarf_data=[]

def scrape():
    soup=BeautifulSoup(browser.page_source,"html.parser")
    brown_dwarf_table=soup.find_all("table", attrs={"class","wikitable sortable jquery-tablesorter"})
    t_body=brown_dwarf_table.find('tbody')
    t_rows=brown_dwarf_table.find_all('tr')

    for row in t_rows:
        t_col=row.find_all('td')
        temp_list=[]
        for col_data in t_col:
            data=col_data.text.strip()
            temp_list.append(data)
        dwarf_data.append(temp_list)
temp_list[]