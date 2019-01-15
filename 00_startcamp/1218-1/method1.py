my_list = [4,7,9,1,3,6]
#최대 값
max(my_list)
#최소 값
min(my_list)

#특정 요소의 인덱스. ?
my_list.index()
#리스트를 뒤집으려면?
my_list.reverse()
#my_list.???()# method 라고 부른다.

class object
dust=100 #int
language = 'python' #str
samsung = ['sds','electronics','s1']#list
samsung.index('sds')#오브젝트가 할수있는 함수

lang = 'python'
#메서드에는 원본을 그대로 유지하고 아웃풋을 내는 경우와 원본을 바꾸는 경우가 있다.
lang.capitalize()#대문자로 바꾼다.(원본유지)
lang.replace('on','off')#문자를 바꾼다.(원본유지)
lang.sort()#소팅을한다. 오름차순 (원본을 바꾼다.)
samsung.append('bio')#추가를한다.(원본을 바꾼다.)
