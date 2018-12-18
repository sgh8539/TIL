# 1218 수업정리 

## 1.개발환경 설정

* chocolately
  * 윈도우 패키지 매니저.
* python
* git
* vscode
  * 크롬부라우저
* chrome

## 2. 리스트
### 리스트 만들기
``````python
bat = [
    ['spiderman'],
    ['ironman','captinamerica'],
    ['docter','nurse'],
    ['good']
]
``````
* list 안에 list를 정리하려면 어케해야되나
  * mcu=bat[1], bat[1][2] 형식으로 접근
### 리스트 추출하기

1. [0]처럼 인덱스접근하기
2. [1:10] 처럼 인덱스 접근하기

###리스트 +딕셔너리
``````python
my_info = {
    'name' : 'neo',
    'job' : 'hacker',
    'mobile' : '01012312344',
    'email' : 'sgh8539@naver.com'
}

hphk = [
    {
        'name' : "song"
        'job' : 'hacker'
    },
    {
        'name' : "kim"
        'job' : 'none'
    }
]
``````
* print (my_info['email']) # dic의 data loading-sgh8539@naver.com
* print (hphk[1]['name']) # list+dic의 data loading-kim
* type(hphk[1]) # dict가뜬다
* hphk[1]#list 정수 검색조건 = index

###리스트연산
``````python
team = [
    'john',10000,
    'neo',100,
    'tack',40500
]
team[-1]#40500
type(team[2:4])#list
a = [1] #한개라도 list type이다

new_memeber = [
    'js', 10
]
``````
* team += new_memeber# n=n+1 == n+=1
* print(team)#앞의 리스트 맨뒤(안으로)로 합쳐진다.
## 3. 함수(Function)
### 
``````python
print('hi')
len('hi')
len([1,2,3,4,5])
del()
type('a')
scores = [45,60,78,88]
high_score = max(scores)
round(1.8)#반올림
round(1.876,2)#둘째자리 전까지 반올림
low_score = min(scores)
print(low_score)
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
full = first+second
full_sorted = sorted(full)
help()
reverse_sorted = sorted(full,reverse=True)
print (reverse_sorted)
``````
##4. 메소드
###
* 메서드는 함수다 다만 주어 동사() 형식으로 이루어지며 주어 자리에 오는 object 들이 할수 있는 행동들이다.

| str  | int  | bool | list | dict | class들이다. |
| ---- | ---- | ---- | ---- | ---- | ------------ |
|      |      |      |      |      |              |



