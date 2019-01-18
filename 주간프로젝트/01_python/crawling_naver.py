# -*- coding: utf-8 -*-
'''
3번 문제

영화별로 다음과 같은 내용을 저장합니다.
영진위 영화 대표코드, 영화 썸네일 이미지의 URL, 하이퍼텍스트 link, 유저 평점 
해당 결과를 movie_naver.csv에 저장합니다. 
'''

'''
4번문제
이미지 URL
응답
응답받은 결과를 파일로 저장합니다. 
저장시 반드시 wb 옵션으로 저장하시기 바랍니다. 
저장되는 파일명은 images 폴더 내에 진위 화 대표코드.jpg 입니다. 
'''
################3번문제
import requests
import json
import csv
from time import sleep

code = {'20184105': '말모이', '20176251': '내안의 그놈', '20189463': '주먹왕 랄프 2: 인터넷 속으로', '20180290': '아쿠아맨', '20183915': '극장판 공룡메카드: 타이니소어의 섬', '20185485': '보헤미안 랩소디', '20184574': '그린 북', '20186281': '범블비', '20170658': 'PMC: 더 벙커', '20175547': '스윙키즈', '20183785': '점박이 한반도의 공룡2 : 새로운 낙원', '20184187': '언니', '20182421': '그린치', '20168773': '마약왕', '20183479': '극장판 짱구는 못말려: 아뵤! 쿵후 보이즈 ~라면 대란~', '20183238': '스파이더맨: 뉴 유니버스', '20177552': '국가부도의 날', '20179230': '도어락', '20183375': '극장판 포켓몬스터 모두의 이야기', '20189843': '호두까기 인형과 4개의 왕국', '20182082': '부탁 하나만 들어줘', '20178825': '모털 엔진', '20183745': '런닝맨 : 풀룰루의 역습', '20177538': '완벽한 타인', '20184481': '성난황소', '20181905': '후드', '20176814': '신비한 동물들과 그린델왈드의 범죄', '20183073': '베일리 어게인', '20181171': '바울', '20183007': '거미줄에 걸린 소녀', '20182966': '투 프렌즈', '20183050': '번 더 스테이지: 더 무비', '20182935': '출국', '20182669': '툴리', '20186822': '너의 췌장을 먹고 싶어', '20170513': '동네사람들', '20189869': '해피 투게더', '20174981': '창궐', '20010291': '해리포터와 마법사의 돌', '20179006': '여곡성', '20181404': '벽 속에 숨은 마법시계', '20180523': '스타 이즈 본', '20182693': '구스범스: 몬스터의 역습'}

naver_URI = 'https://openapi.naver.com/v1/search/movie.json?query='
client_id = 
client_secret = '' 
headers = {'X-Naver-Client-Id' : client_id ,'X-Naver-Client-Secret': client_secret}
result_3 = []

for i in code.keys():
    res = requests.get(naver_URI + code[i], headers = headers)
    data = res.json()
    # title = data['items'][0]['title']
    img = data['items'][0]['image']
    link = data['items'][0]['link']
    score = data['items'][0]['userRating']
    result_3 += [i,img,link,score]
    sleep(0.05)

imageurl = []

f = open('./movie_naver.csv','w+',encoding='utf-8' ,newline ='')
writer = csv.writer(f)
for i in range(len(result_3)//4):
    imageurl += [result_3[i*4+1]]
    writer.writerow(result_3[i*4:i*4+4])
f.close()

print(imageurl)
imageurl = ['https://ssl.pstatic.net/imgmovie/mdi/mit110/1717/171755_P39_140011.jpg']
###################4번문제
import urllib

for i in range(len(imageurl)):
    urllib.request.urlretrieve(i,f'{i}.jpg')
