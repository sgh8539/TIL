import random
import requests
import os, sys, time
#내 번호
def pick_lotto():
        numbers = random.sample(list(range(1,46)),6)
        return numbers

#로또번호
def get_lotto(draw_no):# arguments = 인자로 들어오게 되는 값  = args
        url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="+str(draw_no)
        response = requests.get(url)
        data = response.json()
        real_numbers = []
        for i in data:
                if 'drwtNo' in i :
                        real_numbers.append(data[i])
                elif 'bnusNo' in i:
                        bnus_numbers = data[i]
        # real_bnus_numbers.update({'numbers':real_numbers})
        # real_bnus_numbers.update({'bonus':bnus_numbers})
        real_bnus_numbers = {'numbers':real_numbers,'bonus':bnus_numbers}
        return real_bnus_numbers

#로또 당첨 확인
def am_i_lucky(pick, draw):
        # 인수값 측정 준비
        real_numbers_new = set(draw['numbers'])
        temp_numb = set(pick)
        bnus_numbers = set([draw['bonus']])
        # 인수값 측정
        match = len(real_numbers_new & temp_numb)
        bnus = len(bnus_numbers & temp_numb)

        if match==6:
                score = '1등'
        elif match==5 and bnus==1:# and bonus in my_numbers
                score = '2등'
        elif match==5:
                score = '3등'
        elif match==4:
                score = '4등'
        elif match==3:
                score = '5등'
        else:
                score = '꽝'
        return score


# #뽑은 함수값
# num = int(input('로또회차입력 : '))

# if num > 837:
#         print('아직 자료가 없습니다.')
#         sys.exit(1)
# else:
#         my_numbers = pick_lotto()
#         real_numbers = get_lotto(num)
# #프린트 
# print(sorted(my_numbers))
# print(sorted(real_numbers['numbers']))
# print (am_i_lucky(my_numbers, real_numbers))


