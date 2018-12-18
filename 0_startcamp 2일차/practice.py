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

# for key, value in data.items():
#     if 'drwtNo' in key:
#         real_numbers.append(value)
for i in data:
    print(i)
real_numbers.sort()




# real_numbers = [
#     data['drwtNo1'],
#     data['drwtNo2'],
#     data['drwtNo3'],
#     data['drwtNo4'],
#     data['drwtNo5'],
#     data['drwtNo6']

# ]


print ()