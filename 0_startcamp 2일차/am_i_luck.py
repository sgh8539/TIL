import random
import requests

numbers = list(range(1,46))
my_numbers=random.sample(numbers,6)
sort_numbers=my_numbers.sort()


url = "https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837"
response = requests.get(url, verify=False)
data = response.json()
real_numbers = []

for i in data:
    if 'drwtNo' in i :
        real_numbers.append(data[i])
var=0
# for i in data:
#     if data[i] == sort_numbers[i]:
#         val+=1

print(data)
print(sort_numbers)
print(real_numbers)

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
