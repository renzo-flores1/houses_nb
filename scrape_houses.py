# Load libraries
import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# initialize dataframe
column_names = ["Address", "Beds", "Baths", "House Size", "Lot Size", "Type", "Price"]
house_info = pd.DataFrame(columns = column_names)


# URL pages

# there are 31 pages containing the houses
for i in range(1,31):
        page = f"https://www.point2homes.com/CA/Real-Estate-Listings/NB.html?page={i}"

        # open page
        http = urllib3.PoolManager()
        req = http.request('GET',page)


        soup = BeautifulSoup(req.data, 'html.parser')

        # get list of houses
        houses = soup.find_all('article')

        for house in houses:
                address = house.find_all('div', class_ = 'address-container')[0]['title']

                # remove characters such as for sale in
                # because it is not an address
                address = address[address.find("sale in"):][8:]

                beds = house.find('li',class_='ic-beds')
                if beds is not None:
                        beds = int(beds.find("strong").text)
                else:
                        beds = np.nan


                baths = house.find('li',class_='ic-baths')
                if baths is not None:
                        baths = int(baths.find("strong").text)
                else:
                        baths = np.nan

                houseSize = house.find('li',class_='ic-sqft')
                if houseSize is not None:
                        houseSize = houseSize.find("strong").text
                        houseSize = houseSize.replace(",","")
                        houseSize = int(houseSize)
                else:
                        houseSize = np.nan

                lotSize = house.find('li',class_='ic-lotsize')
                if lotSize is not None:
                        lotSize = lotSize.find("strong").text
                        lotSize = lotSize[:-3]
                        lotSize = float(lotSize)
                else:
                        lotSize = np.nan


                houseType = house.find('li',class_='property-type ic-proptype').text

                price = house.find('div',class_='price')
                price_val = price['data-price']

                price_val = price_val[1:-4]
                price_val = price_val.replace(",","")
                price_val = int(price_val)

                df = pd.DataFrame({"Address": address, "Beds": beds,
                                   "Baths": baths, "House Size": houseSize,
                                   "Lot Size": lotSize,
                                   "Type": houseType,
                                   "Price": price_val},index=[0])

                house_info = house_info.append(df)


print(house_info.shape)
house_info.to_csv("houseprices_nbf.csv",index=False)
