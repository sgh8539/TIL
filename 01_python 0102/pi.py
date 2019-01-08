result=[]
remain = 0 
a = 'R R G B R G B B'.split(' ')

def RGBfun(a):
    remain = 0
    result = []
    if type(a)==str:
        a = a.split(' ')
    if len(a)==1:
        return a
    else:
        for i in a:
            if remain == 0:
                remain = i 
            elif remain == i:
                if i=='R':
                    result.append('R')
                elif i=='G':
                    result.append('G')
                else:
                    result.append('B')
                remain=i
            elif remain != i:
                if i=='R':
                    if remain=='B':
                        result.append('G')
                    else:
                        result.append('B')
                elif i=='G':
                    if remain=='B':
                        result.append('R')
                    else:
                        result.append('B')
                else:
                    if remain=='G':
                        result.append('R')
                    else:
                        result.append('G')
                remain=i

        return RGBfun(result)
    
print(RGBfun('R R G B R G B B'))
