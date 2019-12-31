import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.google.co.kr/search?q=%EB%B9%B5&sxsrf=ACYBGNSBFV94g5so4lVSQHYP04dcpYM4-A:1577779758321&source=lnms&tbm=vid&sa=X&ved=2ahUKEwjI2pzQt9_mAhVlNKYKHQfRDewQ_AUoA3oECA4QBQ&biw=1440&bih=789', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tbody들을 불러오기
breads = soup.select('#rcnt > div.col > #center_col > div.med > #search > div > div > div > div > div')
# print (breads)

for bread in breads:
    # print (show)
    bread_image = bread.select_one('div > div.s > div > div')
    print (bread_image)
    bread_title = bread.select_one('h3.LC20lb')
    # print (bread_title.text)
