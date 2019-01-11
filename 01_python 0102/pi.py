def hanoi(n,current=[],change=3):
    if current == []:
        current = [1 for i in range(n)]
    result = []
    if n==1 and change == 3:
        current[0]=3
        result.append(list(current))
        return result
    if n==1 and change == 2:
        current[0]=2
        result.append(list(current))
        return result
    if n==1 and change == 1:
        current[0]=1
        result.append(list(current))
        return result

    else:
        if change==3:
            if current[0]==2:
                k = hanoi(n-1,current,1)
                current[n-1]=3
                l=[list(current)]
                c = hanoi(n-1,current,3)
            else:
                k = hanoi(n-1,current,2)
                current[n-1]=3
                l=[list(current)]
                c = hanoi(n-1,current,3)            
            return k+l+c        
        
        elif change==2:
            if current[0]==1:
                k = hanoi(n-1,current,3)
                current[n-1]=2
                l=[list(current)]
                c = hanoi(n-1,current,2)
            else:
                k = hanoi(n-1,current,1)
                current[n-1]=2
                l=[list(current)]
                c = hanoi(n-1,current,2)
            return k+l+c         
        
        elif change==1:
            if current[0]==2:
                k = hanoi(n-1,current,3)
                current[n-1]=1
                l=[list(current)]
                c = hanoi(n-1,current,1)
            else:
                k = hanoi(n-1,current,2)
                current[n-1]=1
                l=[list(current)]
                c = hanoi(n-1,current,1) 
            return k+l+c

def hanoiFirst (n) :
    current = [1 for i in range(n)]
    return [current] + hanoi(n)

print(hanoiFirst(5))

