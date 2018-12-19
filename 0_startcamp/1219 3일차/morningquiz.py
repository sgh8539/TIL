print('good morning')
#1 평균을 구해라

my_score = [79, 84, 66, 93]
your_scorenumb=[]

your_score ={
    '수학' : 87,
    '국어' : 83,
    '영어' : 76,
    '도덕' : 100
}
for key in your_score:
    if(key=='수학','국어','영어','도덕'):
        your_scorenumb.append(your_score[key])

my_average=sum(my_score,0.0)/len(my_score)
your_average=sum(your_scorenumb)/len(your_scorenumb)

a=your_score.values()#value 값만뽑아낸다.

print(a)
print(len(a))
print(your_score)

print(my_average)
print(your_average)

items = [8, 23, 45, 12, 78]
for i, va in enumerate(items):
    print (i, va)


print(str(enumerate(items)))#인덱스와 함께 열거하는 함수
# insert
# append
# +
# extend
# del
# remove
