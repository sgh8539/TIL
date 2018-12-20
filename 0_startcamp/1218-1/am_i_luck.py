import random
import requests

numbers = list(range(1,46))
my_numbers=random.sample(numbers,6)
my_numbers.sort()


url = "https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837"
response = requests.get(url, verify=False)
data = response.json()
real_numbers = []
bnus_numbers = []

for i in data:
    if 'drwtNo' in i :
        real_numbers.append(data[i])
    elif 'bnusNo' in i:
            bnus_numbers.append(data[i])

real_numbers.sort()

# var=0
# for i in data:
#     if data[i] == sort_numbers[i]:
#         val+=1
print(data)

print(my_numbers)
print(real_numbers)
print(bnus_numbers)
var1=[0,1,2,3,4,5]
var2=[0,1,2,3,4,5]
a=0
b=0
c=0
for i in var1 :
        for j in var2 :
                if (real_numbers[j] == my_numbers[i]):
                        a+=1
for i in var2:
                if (my_numbers[i] == bnus_numbers[0]):
                        b+=1
print(a)
print(b)

if (a==6 and b==0):
        print ('1등')
elif (a==5 and b==1):
         print('2등')
elif (a==5):
        print('3등')
elif (a==4):
         print('4등')
elif (a==3):
        print('5등')
else:
        print('꼴등')

# if (a==5 and b==1):
#         print('2등')
# elif (a<3):
#         print('꽝')
# else        
#         print(str(7-a)+'등')






# for key, value in data.items():
#     if 'drwtNo' in key:
#         real_numbers.append(value)
#my numbers, realnumbers bounus numbers
#1등 : my_numbers == real numbers
#2등 : 5개 my 나머지 하나 보너스넘버
#3등 : 5
#4등 : 4
#5등 :3
#꽝
