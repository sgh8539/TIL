import random
import requests

# 로또
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

# real_numbers=[2, 25, 28, 30, 33, 45]
# k=0
# a=0
# b=0
# intersection=0
# while intersection<3:
#         k+=1
#         intersection = len(list(set(my_numbers).intersection(real_numbers)))


#내 해답 
# for i,va in enumerate(my_numbers):
#         for j,vr in enumerate(real_numbers) :
#                         if real_numbers[j] == my_numbers[i]:
#                                 a+=1
# for i,va in enumerate(my_numbers):
#         if my_numbers[i] == bnus_numbers[0]:
#                         b+=1


if a==6:
        print ('1등')
elif a==5 and b==1:# and bonus in my_numbers
         print('2등')
elif a==5:
        print('3등')
elif a==4:
         print('4등')
elif a==3:
        print('5등')
else:
        print('꼴등')

#
#intersection_bnus = len(list(set(my_numbers).intersection(bnus_numbers)))


# #해답 1
# count = 0
# for my_number in my_numbers :
#         for real_number in real_numbers:
#                 if my_number == real_number:
#                         count += 1
# print(count)


# list = [1,2,3]
# tuple = (1,2,3)
# set = {1,2,3} - 순서가 없으니 index가 없다.

# #해답 1-2

