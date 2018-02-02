
import requests
from bs4 import BeautifulSoup
import pandas
import re

from matplotlib import pyplot as PLT
import numpy as NP

res = requests.get('https://www.coingecko.com/chart/1/usd.json?locale=zh-tw')
print(type(res.json()))
print(res.json())

m = re.search('(\[\[.*?\]\])', res.text)


price_str = eval(m.group(1).replace('null', 'None'))


df = pandas.DataFrame(price_str)

print(df)

df.columns = ['time', 'price']
df.index= df['time']
df['price'].describe()



print(df[['price']].plot(kind = 'line'))