import re
import os
inputequation='12x+26x'
found=(re.findall(r'\d+',inputequation))
# print(found)
rf=re.split('\d',inputequation)
# print(rf[1:-1])
res_str = re.sub(r"^\d.\d|\d+", r"({@})", inputequation)
# i need it to return back the same numbers... so time to make an array

# print(res_str)


start=97
end=start+len(found)
total=[]
for i in range (start,end):
    # print(chr(i))
    total.append(chr(i))

# print(total)


formatted_eq1= re.sub('\@', lambda a, rep=iter(total): next(rep), res_str)
# print(formatted_eq1)

lis=[]
lis.append(f'''import subprocess
import colorama
from colorama import *''')
for i in range(len(found)):
    # print(total[i],'=',found[i])
    lis.append("\n"+total[i]+'='+found[i])

lis.append(f'''\nformula=f'{formatted_eq1}\'
subprocess.call(['qalc',f'{{formula}}'])
process1 = subprocess.run(['qalc','-t',f'{{formula}}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
sol=(colorama.Fore.RED + process1.stdout.decode())
print(str( sol ))
''')
f=(''.join(lis))

# print(f)


for i in range(1,99):
    path = f'file{i}.py'
    filewriter = os.path.exists(path)

    if filewriter == False:
        print(f'Written to file{i}.py!')
        file1 = open(f'file{i}.py', 'w')
        file1.write(f)
        file1.close()
        break;
    if filewriter==True:
        # print(f'file{i}.py exists...')
        pass;
