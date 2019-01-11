class Diction:
    diction = {
        'apple' : '사과',
        'banana' : '바나나',
    }
    def diction_comment(self, word):
        if word in self.diction.keys():
            return f'{word}은(는){self.diction[word]}!'
        else:
            return f'{word}은(는) 나만의 단어장에 없는단어입니다.'