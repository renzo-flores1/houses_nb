
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import urllib3

df = pd.read_csv("houseprices_nbf.csv")

# df['Type'] has '\r\n' at the beginning and end, so we remove it
df['Type'] = df['Type'].str.replace(r'\\r\\n','')

# make column for postal code
# use only first 3 characters
# for instance E3A or E3B if in Fredericton
df['Postal Code'] = np.nan

# open Wikipedia for Canadian postal codes
page = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_E'
http = urllib3.PoolManager()
req = http.request('GET',page)

soup = BeautifulSoup(req.data, 'html.parser')

# create a dictionary for city and postal code
postal = {}
postal_codes = soup.select('span[style="line-height: 125%"]')

for code in postal_codes:
    postal_code = code.text[:3]
    city = code.text[3:]
    postal[city] = postal_code

print(postal)


for index, address in df['Address'].items():
    if address[-7] == E and address[-6].isnumeric():
        df['Postal Code'][index] = address[-7:-4]
    else:
