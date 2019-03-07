import sys
from math import log, floor

for primer, i in enumerate(map(int, sys.stdin.readlines())):
    st = log(3, 10) + (i * log(1.5, 10)) #izračunamo
print('Case ' + str(primer + 1) + ':', floor(st + 1))#pazimo kako more izgledati zapis 
