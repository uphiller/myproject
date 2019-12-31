import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EA%B3%B5%EC%97%B0', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tbody들을 불러오기
shows = soup.select('div.sc.cs_nperformance._cs_nperformance > div.nperformace_wrap > div.info_box.list > div.list_area > div.list_card._APIList > ul > li ')
#왠지모르게 안됨
#songs = soup.select('#main_pack > div.sc.cs_nperformance._cs_nperformance')
#print (songs)

for show in shows:
    # print (show)
    show_image = show.select_one('div.list_thumb > a > img')
    print (show_image['src'])
    show_title = show.select_one('div.list_title > strong > a')
    #print (show_title.text)
