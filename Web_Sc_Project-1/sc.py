from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"

# Webdriver
browser = webdriver.Chrome()
browser.get(START_URL)
time.sleep(10)

scrapped_data = []

def scrape():
               
        # BeautifulSoup Object     
        soup = BeautifulSoup(browser.page_source, "html.parser")

       
        # Find <table>
        bright_star_table = soup.find("table", attrs={"class", "wikitable sortable sticky-header jquery-tablesorter"})
        
        # Find <tbody>
        table_body = bright_star_table.find('tbody')

        # Find <tr>
        table_rows = table_body.find_all('tr')

        # Get data from <td>
        for row in table_rows:
            table_cols = row.find_all('td')
                
            temp_list = []

            for col_data in table_cols:
                
                # print(col_data.text)

                
                data = col_data.text.strip()
                # print(data)

                temp_list.append(data)

            
            scrapped_data.append(temp_list)
                


# Calling Method    
scrape()
stars_data = []


for i in range(0,len(scrapped_data)):
    
    Star_names = scrapped_data[i][2]
    Distance = scrapped_data[i][4]
    Bayers = scrapped_data[i][3]
    Visual_Magnitude = scrapped_data[i][1]
    Lum = scrapped_data[6]

    required_data = [Star_names, Distance, Bayers, Visual_Magnitude, Lum]
    stars_data.append(required_data)

print(stars_data)


# Define Header
headers = ['Star_name','Distance','Bayers','Visual_Magnitude','Luminosity']  

# Define pandas DataFrame   
star_df = pd.DataFrame(stars_data, columns=headers)

#Convert to CSV
star_df.to_csv('scra_data.csv',index=True, index_label="id")