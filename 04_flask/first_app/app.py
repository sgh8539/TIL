# from flask import Flask, jsonify
import flask
from dictionary_ssafy import Diction

import random


app = flask.Flask(__name__)#__ 뜻은 str하나넣어줬는데 가변적이다.

@app.route('/')#@ == 데코레이터 고급문법 알아서 알아봐라이말이야# 라우트 라우팅
def index():
    return 'hi'
#@ 데코레이터가 붙어있으면 플라스크 서버에서 길을 뚫어놨는데 들어오면은 밑에 def함수를 실행시켜라!!! 일봉에 조건문 만약에 어플리케이션 플라스크서버에
#들어오면 실행해라 원래라면 if밑에실행문잉 있어야 되는데 @마크는 그냥 실행시킨다. 추후에 설명한다.



#워크샵
@app.route('/dictionary/<string:word>')#variable routing
def dictionary(word):    
    a = Diction()
    b = a.diction_comment(word)
    return b


@app.route('/lotto')
def lotto():
    current = random.sample(range(1,46),6)
    return flask.jsonify(current)


@app.route('/ssafy')
def ssafy():
    return 'sssssssssssafy'

@app.route('/hi/<string:name>')
def hi(name):
    return f'hi {name}'


if __name__ == '__main__':
    print('__name__is__main__')
    app.run(debug=True)
else:
    print('unknown')