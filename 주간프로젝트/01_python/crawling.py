


'''
1번문제
targetDT=20190113

http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=aec6ca960ace19426160722ef631bec6&targetDt=20190113

http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt=20120101
http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt=20120101


movieCd
movieNm
audiAcc :누적 관객수
해당일



수집된 데이터에서 화 대표코드, 화명, 해당일 누적관객수, 해당일을 기록합니다.
해당일 누적관객수는 중복시 최신 정보를 반하여야 합니다. 예) 화 아쿠아맨이 20190113 
기준 50,000명이고, 20190106 기준 5,000명이면 50,000명이 저장되어야 합니다. 

해당 결과를 boxoﬃce.csv 에 저장합니다. 
'''

'''
2번문제
영화별로 다음과 같은 내용을 저장합니다. 
영화 대표코드, 영화명(국문), 영화명(영문), 영화명(원문) , 개봉연도, 상시간, 장르, 감독 명, 관람등급, 배우1, 배우2, 배우3 배우의 경우 최대 3명입니다. 
영화에 따라 1~2명일 수도 있습니다. 

http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=430156241533f1d058c603178cc3ca0e&movieCd=20124079


해당 결과를 movie.csv에 저장합니다. 

'''

######################1번문제

import requests
import json
import csv

key = 'aec6ca960ace19426160722ef631bec6'
date = [20190113,20190106,20181230,20181223,20181216,20181209,20181202,20181125,20181118,20181111]
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
print (result)
code = {}

f = open('./boxoﬃce.csv','w+',encoding='utf-8' ,newline ='')
writer = csv.writer(f)
for i in range(len(result)//4):
    code[result[i*4]] = result[i*4+1]
    writer.writerow(result[i*4:i*4+4])
f.close()

print (code)


########################2번문제
# import requests
# import json
# import csv
# code_2 = code.keys()
# code = ['20184105','20176251', '20189463', '20180290', '20183915', '20185485', '20184574', '20186281', '20170658', '20175547', '20183785', '20184187', '20182421', '20168773', '20183479', '20183238', '20177552', '20179230', '20183375', '20189843', '20182082', '20178825', '20183745', '20177538', '20184481', '20181905', '20176814', '20183073', '20181171', '20183007', '20182966', '20183050', '20182935', '20182669', '20186822', '20170513', '20189869', '20174981', '20010291', '20179006', '20181404', '20180523', '20182693']
# key = 'aec6ca960ace19426160722ef631bec6'
# f = open('movie.csv','w+',encoding='utf-8' ,newline ='')
# writer = csv.writer(f)

# for i in code_2:
#     result_2=[]
#     URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={i}'
#     res = requests.get(URL).json()
#     data = res['movieInfoResult']['movieInfo']
#     b=[]

#     a = [
#         i,
#         data['movieNm'], 
#         data['movieNmEn'],
#         data['movieNmOg'], 
#         data['openDt'], 
#         data['showTm'],
#         data['genres'][0]['genreNm'],
#         data['directors'][0]['peopleNm'],
#         data['audits'][0]['watchGradeNm'],
#     ]
#     if len(data['actors']) != 0 :
#         for i in range(len(data['actors'])):
#             b+=[data['actors'][i]['peopleNm']]
#             if i == 2:
#                 break
#     else:
#         b+=[]
#     result_2 += a+b
#     writer.writerow(result_2)
# f.close()

    







