import requests
from bs4 import BeautifulSoup

res = requests.get('https://github.com/ywchiu/tibamepy/blob/master/data/trump.txt')

print(res.text)

''''''''