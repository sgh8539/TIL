city_temp = {
    '서울' : [-6, -10, 5],
    '대전' : [-3, -5, 2],
    '광주' : [0, -5, 10],
    '구미' : [2, -2, 9]
}

#items
#tuple
#set
#list
#dictionary
#city_temp.items() #tuple?

#3-1
print("3번문제")
all_temp=[]
all_city=[]
for i ,j in city_temp.items():
    avg=round(sum(j)/len(j),2)
    print(i,':',avg)

#4-1
all_temp=[]
for key, value in city_temp.items():
    all_temp += value

highest = max(all_temp)
lowest = min(all_temp)
print(highest, lowest)

hottest = []
coldest = []

for a, b in city_temp.items():
    if highest in b:
         hottest.append(a)
    if lowest in b:
         coldest.append(a)

print(hottest, coldest)

#4-2
ak = -100
bk = 100
print("4번문제")
for i ,j in city_temp.items():
    a = max(j)
    b = min(j)
    if ( ak < a ):
        ak = a 
        aik = i
    if ( bk > b ):
        bk = b
        bik = i
print('hottest',ak,aik)
print('coldedst',bk,bik)







# for i in city_temp:
#     all_city.append(i)
#     all_temp.append(city_temp[i])
#     sum_temp = sum(city_temp[i])
#     avg_temperature = round(sum_temp/len(city_temp[i]),2)
#     print(i,":",avg_temperature)


# #4 도시중에 최근 3일간 가장 추었던곳 가장 더웠
# # print("4번문제")
# # for i, va in enumerate(all_temp):
# #     if (max(all_temp)==va):
# #         a=i
# # for i, va in enumerate(all_temp):
# #     if (min(all_temp)==va):
# #         b=i
# # print(all_temp)
# # print(all_city)
# # print('Hottest:',all_city[a],max(all_temp))
# # print('Coldest:',all_city[b],min(all_temp))



# #5 
# print("5번문제")
# city_value=city_temp.values()
# city_key=city_temp.keys()
# list_value=list(city_value)
# list_key=list(city_key)

# temp_max=[]
# temp_min=[]
# for i, va in enumerate(list_value):
#         temp_max.append(max(list_value[i]))
# for j, vr in enumerate(list_value):
#         temp_min.append(min(list_value[j]))

# for i, va in enumerate(temp_max):
#     if (max(temp_max)==va):
#         a=i
# for i, va in enumerate(temp_min):
#     if (min(temp_min)==va):
#         b=i
# print()
# print(temp_max)
# print(temp_min)
# print('Hottest:',list_key[a],max(temp_max))
# print('Coldest:',list_key[b],min(temp_min))


