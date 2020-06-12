# Load libraries
import urllib3
from bs4 import BeautifulSoup
import pandas as pd

# URL pages
page = 'https://www.point2homes.com/CA/Real-Estate-Listings/NB.html'

http = urllib3.PoolManager()
req = http.request('GET',page)


soup = BeautifulSoup(req.data, 'html.parser')
print(soup)
