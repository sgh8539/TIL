
###################4번문제
import urllib.request

imageurl = ['https://ssl.pstatic.net/imgmovie/mdi/mit110/1717/171755_P39_140011.jpg']
for i in range(len(imageurl)):
    urllib.request.urlretrieve(i,'s.jpg')
