
'''
1번문제
수집된 데이터에서 화 대표코드, 화명, 해당일 누적관객수, 해당일을 기록합니다.
해당일 누적관객수는 중복시 최신 정보를 반하여야 합니다. 예) 화 아쿠아맨이 20190113 
기준 50,000명이고, 20190106 기준 5,000명이면 50,000명이 저장되어야 합니다. 
해당 결과를 boxoﬃce.csv 에 저장합니다. 

2번문제
영화별로 다음과 같은 내용을 저장합니다. 
영화 대표코드, 영화명(국문), 영화명(영문), 영화명(원문) , 개봉연도, 상시간, 장르, 감독 명, 관람등급, 배우1, 배우2, 배우3 배우의 경우 최대 3명입니다. 
영화에 따라 1~2명일 수도 있습니다. 
해당 결과를 movie.csv에 저장합니다.

3번 문제
영화별로 다음과 같은 내용을 저장합니다.
영진위 영화 대표코드, 영화 썸네일 이미지의 URL, 하이퍼텍스트 link, 유저 평점 
해당 결과를 movie_naver.csv에 저장합니다. 

4번문제
이미지 URL 응답받은 결과를 파일로 저장합니다. 
저장시 반드시 wb 옵션으로 저장하시기 바랍니다. 
저장되는 파일명은 images 폴더 내에 진위 화 대표코드.jpg 입니다

'''
#-----------------------1번문제

import requests
import json
import csv
from time import sleep
import urllib.request
import os

# key = 'aec6ca960ace19426160722ef631bec6'
# client_id = '9lp1WD7TUx1IIV444aNx'
# client_secret = 'z4POQbVAuF' 
# export k_key='aec6ca960ace19426160722ef631bec6'
# export naver_id='9lp1WD7TUx1IIV444aNx'
# export naver_pass='z4POQbVAuF'

key = os.getenv('k_key')
date = [20190113,20190106,20181230,20181223,20181216,20181209,20181202,20181125,20181118,20181111]
naver_URI = 'https://openapi.naver.com/v1/search/movie.json?query='
client_id = os.getenv('naver_id')
client_secret = os.getenv('naver_pass')
headers = {'X-Naver-Client-Id' : client_id ,'X-Naver-Client-Secret': client_secret}
full_data = []
result=[]

for i in map(str, date):
    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={i}&weekGb=0'
    res = requests.get(url).json()
    data = res['boxOfficeResult']['weeklyBoxOfficeList']
    for j in range(len(data)):
        if data[j]['movieCd'] in result:
            continue
        else:
            result += [data[j]['movieCd'], data[j]['movieNm'], data[j]['audiAcc'] ,i]
code = {}

f = open('C:/Users/student/TIL/crawling/boxoﬃce.csv','w+',encoding='utf-8' ,newline ='')
writer = csv.writer(f)
for i in range(len(result)//4):
    code[result[i*4]] = result[i*4+1]
    writer.writerow(result[i*4:i*4+4])
f.close()

#-----------------------2번문제

f = open('C:/Users/student/TIL/crawling/movie.csv','w+',encoding='utf-8' ,newline ='')
writer = csv.writer(f)

for i in list(code.keys()):
    result_2=[]
    URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={i}'
    res = requests.get(URL).json()
    data = res['movieInfoResult']['movieInfo']
    b=[]

    a = [
        i,
        data['movieNm'], 
        data['movieNmEn'],
        data['movieNmOg'], 
        data['openDt'], 
        data['showTm'],
        data['genres'][0]['genreNm'],
        data['directors'][0]['peopleNm'],
        data['audits'][0]['watchGradeNm'],
    ]
    if len(data['actors']) != 0 :
        for i in range(len(data['actors'])):
            b+=[data['actors'][i]['peopleNm']]
            if i == 2:
                break
    else:
        b+=[]
    result_2 += (a+b)
    writer.writerow(result_2)
f.close()

#-----------------------3번문제

result_3 = []

for i in code.keys():
    res = requests.get(naver_URI + code[i], headers = headers)
    data = res.json()
    img = data['items'][0]['image']
    link = data['items'][0]['link']
    score = data['items'][0]['userRating']
    result_3 += [i,img,link,score]
    sleep(0.05)

imageurl = []

f = open('C:/Users/student/TIL/crawling/movie_naver.csv','w+',encoding='utf-8' ,newline ='')
writer = csv.writer(f)
for i in range(len(result_3)//4):
    imageurl += [result_3[i*4+1]]
    writer.writerow(result_3[i*4:i*4+4])
f.close()

#-----------------------4번문제

for index, temp in enumerate(imageurl):
    urllib.request.urlretrieve(temp, f'C:/Users/student/TIL/crawling/img/{list(code.keys())[index]}.jpg')

