year_input = 2019
yoon = year_input%100 != 0 and year_input%4 == 0 or year_input%400 ==0
if yoon :
    calander = [31,29,31,30,31,30,31,31,30,31,30,31]
else:
    calander = [31,28,31,30,31,30,31,31,30,31,30,31]
year = year_input-1
first_number = ((year*365+int(year/4)-int(year/100)+int(year/400))+1)%7

print(year_input,'년')
for j in range(0,12):
    print(f'\n\n        {j+1}월')
    print('일 월 화 수 목 금 토\n'+'---'*7)
    print('   '*first_number,end='')
    for i in range(1,calander[j]+1):
        if (i+first_number)%7==0 and i<10:
            print(i,end='  \n')
        elif (i+first_number)%7==0 and i>9:
            print(i,end=' \n')
        elif i>9:
            print(i,end=' ')
        else:
            print(i,end='  ')
    first_number = (first_number+calander[j])%7



