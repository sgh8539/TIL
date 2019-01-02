import random

a = input()
b = input()
a = int(a)
b = int(b)

def min(var_1, var_2):
    while var_2 > 0 :
        left = var_1 % var_2
        var_1 = var_2
        var_2 = left
    return var_1


if a<b:
    temp = a
    a = b
    b = temp


print (min(a,b) , int((a*b)/min(a,b)) )

