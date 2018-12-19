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
print(my_numbers)
print(real_numbers)
print(bnus_numbers)

a=0
b=0
for i,va in enumerate(my_numbers):
        for j,vr in enumerate(real_numbers) :
                if real_numbers[j] == my_numbers[i]:
                        a+=1
for i,va in enumerate(my_numbers):
                if my_numbers[i] == bnus_numbers[0]:
                        b+=1
print(a)
print(b)

if a==6 and b==0:
        print ('1등')
elif a==5 and b==1:
         print('2등')
elif a==5:
        print('3등')
elif a==4:
         print('4등')
elif a==3:
        print('5등')
else:
        print('꼴등')