import sys


def Delitelji(n):
    '''poiscemo delitelje stevila n'''
    delitelji = [] 
    for i in range(1, n+1): 
        if (n % i) == 0: 
            delitelji.append(i)
    return delitelji 


def tuji_stevili(a, b):
    '''funkcija vrne ali sta števili tuji ali ne'''
    sez1 = Delitelji(a) # poiscemo delitelje za a 
    sez2 = Delitelji(b) # ter za b
    presek = list(set(sez1) & set(sez2)) # poiscemo presek seznamov
    if len(presek) == 1: 
        return True # sta tuji
    else:
        return False #  nista


def stevilo_tujih(n):
    '''vrne stevilo tujih stevil za n '''
    if n > 0:
        rezultat = 0 
        for i in range(1, n): 
            if tuji_stevili(n, i):
                rezultat += 1 
        return rezultat

for vrstica in sys.stdin:
    vrstica = vrstica.strip("\n").split(" ")
    st = int(vrstica[0])
    if st == 0:
        break
    else:
        print(stevilo_tujih(st))
