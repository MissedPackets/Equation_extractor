import re
teststring=input('Enter an equation: ')
found=(re.findall(r'\d+',teststring))
print(found)
rf=re.split('\d',teststring)
print(rf[1:-1])
res_str = re.sub(r"^\d.\d|\d+", r"(@)", teststring)
# i need it to return back the same numbers... so time to make an array

print(res_str)

res = re.sub('\@', lambda m, rep=iter(found): next(rep), res_str)
print(res)
