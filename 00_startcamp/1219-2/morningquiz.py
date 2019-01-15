print('good morning')
#1 평균을 구해라

def average(temperature):
    return round(sum(temperature)/len(temperature),2)

def cube(x):
    return x*x*x

my_score = [79, 84, 66, 93]

your_score ={
    '수학' : 87,
    '국어' : 83,
    '영어' : 76,
    '도덕' : 100
}
your_scorenumb=your_score.values()

my_average = average(my_score)
your_average=average(your_scorenumb)

# a=your_score.values()#value 값만뽑아낸다.

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
