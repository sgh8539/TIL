import webbrowser#파이썬이 가지고있는 웹브라우저기능을 전부 가져온다.

keywords = [
    'idol',
    'coin',
    'sports',
    'game'
]


for keyword in keywords:
    url = 'https://www.google.com/search?q='+keyword
    webbrowser.open_new(url)
n=0
while(n<3):
    print ("안녕")
    n+=1