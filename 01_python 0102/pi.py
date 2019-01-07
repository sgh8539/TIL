coupon = 11


def chicken(n):
    free = 3
    if n<free:
        return (0, n)
    else:
        return (1+chicken(n-free+1)[0], chicken(n-free+1)[1])

a,b=chicken(coupon)
print(f'치킨:{a}\n남은쿠폰:{b}')

def chicchic(coup,free):
    if coup<free:
        return 0,free
    else:
        return(1+chicchic((coup-free+1),free)[0],free)
print(chicchic(100,3))

