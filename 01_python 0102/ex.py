# def printer_error(s):
#     k = 'abcdefghijklm'
#     b = len(s)
#     a = len([i for i in range(len(s)) if i not in k]) 
    
    
#     return f'{a}/{b}'

# printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")

k = 'abcdefghijklm'
s = 'aaaxxx'
print ([i for i in s if i not in k])
b = s.count('a')
print(b)

def filter_list(l):
    return [i for i in l if type(i) == int]

print(filter_list([1,2,'a','b']))