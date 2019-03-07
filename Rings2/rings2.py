import sys

def izpisi(mreza, letnica):
    razmik = 2 if letnica < 10 else 3 
    for vrstica in mreza:
        vrsticniNiz = ""
        for znak in vrstica:
            if znak == 0:
                vrsticniNiz += "." * razmik
            elif znak < 10:
                vrsticniNiz += "."*(razmik-1) + str(znak)
            else:
                vrsticniNiz += "." + str(znak)
        print(vrsticniNiz)

def Ustreznost(mreza, i, j, letnica):
    d = [letnica-1, letnica] 
    if mreza[i][j-1] in d and mreza[i][j+1] in d and mreza[i-1][j] in d and mreza[i+1][j] in d:
        return True #ce so bili vsi ustrezni, je vrednost resnicna
    return False #sicer nesersnicna

def narediLetnice(n, m, mreza):
    kolikoSpremembJeBilo = 0
    for letnica in range(2, 51): #bomo jo potem breaknili predcasno, ce bo mozno
        for i in range(0, n): # [0, n) ker zacnemo pri 0
            for j in range(0, m): #gledamo vrsticne nize
                # i, j sta indeks vrstice, indeks stolpca
                if mreza[i][j] == 0 or i in [0, n-1] or j in [0, m-1]:
                    continue
                if Ustreznost(mreza, i, j, letnica):
                    mreza[i][j] = letnica
                    kolikoSpremembJeBilo += 1
        if kolikoSpremembJeBilo == 0:
            break #nimamo vec kaj za narediti, lahko vrnemo podatke
        else:
            kolikoSpremembJeBilo = 0 #ocitno se nismo koncali s urejanjem letnic
    return mreza, letnica # vrne se maksimalno letnico
                            
def v_par(niz):
    seznam = [int(stevilo) for stevilo in niz.split(" ")]
    return seznam[0], seznam[1] 
            
vrstice = [vrstica.strip() for vrstica in sys.stdin] # da nimamo \n znakov na koncu vsake
n, m = v_par(vrstice[0]) 
mreza = [] #tukaj bomo dodajali vrstice
for niz in vrstice[1:]:
    vrstica = [] 
    for znak in niz: #gledamo vrstične nize
        if znak == ".": vrstica.append(0)
        elif znak == "T": vrstica.append(1) 
    mreza.append(vrstica)
    
urejenaMreza, letnica = narediLetnice(n, m, mreza)
izpisi(urejenaMreza, letnica)
