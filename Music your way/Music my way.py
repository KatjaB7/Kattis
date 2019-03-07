import sys

prelom = 1
seznamP =[]
seznamU =[]
u = 0

for vrstica in sys.stdin:
    #lastnosti ki jih bodo imele pesmi
    try:
        int(vrstica.rstrip())
        prelom += 1
    except:
        if prelom == 2:
            seznamP.append(vrstica.rstrip())
        if prelom == 3:
            seznamU.append(vrstica.rstrip())

    if prelom ==0:
        naslovIme = vrstica.rstrip() #potrebujemo za izpisovanje
        naslov = (vrstica.rstrip().split(' ')     

for u in seznamU:
    i = 0
    #katera pesem po vrsti lastnosti nas zanima
    while urejanje != naslov[i]:
        i += 1
    urejeno ={}
    for pesem in seznamP:
        el = pesem.split('')
        if el[i] in urejeno: # že obstaja pesem ki ima tako lastnost
            (urejeno[el[i]]).append(pesem)
        else:
            urejeno[el[i]] = [pesem]
    urejenaG=  sorted(urejeno)
    print(naslovIme)
    
    p =0
    nov = {}
    for geslo in urejenaG:
        for pesem in urejeno[geslo]:
            if p == len(seznamP) - and u != len(seznamU) -1:
                print(pesem)
                print()
                nov.append(pesem)
            else:
                print(pesem)
                nov.append(pesem)
            p = p+1
    u = u+1
    seznamP = nov
                
        
