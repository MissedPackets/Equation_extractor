import subprocess
import colorama
from colorama import *

a = 9
b = 25
formula=f'({a})x+({b})x'
print(formula)


subprocess.call(['qalc',f'{formula}'])


# colorama.init(autoreset=True)
out = subprocess.run(['qalc','2+2'], capture_output=True)
print(out)
process = subprocess.run(['qalc','-t','25x'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# m=(colorama.Fore.RED + process.stdout.decode())
process2 = subprocess.run(['qalc','-t','25x'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
m2=(colorama.Fore.RED +process.stdout.decode()+ process2.stdout.decode())
print(str( m2 ))




import colorama
import subprocess
# colorama.init(autoreset=True)
out =subprocess.run(['hostname'], capture_output=True)
print('hi '+colorama.Fore.GREEN + out.stdout.decode())
