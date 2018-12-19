team = [
    'john',10000,
    'neo',100,
    'tack',40500
]
team[-1]#40500
type(team[2:4])#list
a = [1] #한개라도 list type이다

new_memeber = [
    'js', 10
]

team += new_memeber# n=n+1 == n+=1 #리스트 안으로로 합쳐진다.
del(team[2:4])#리스트에서 지운다
print(len(team))
print(team)



