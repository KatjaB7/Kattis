import sys

niz_kart = input()
karte = {'P': set(), 'K': set(), 'H': set(), 'T': set(),}

dolžina = len(niz_kart)

for i in range(dolžina//3):
    karta = niz_kart[i*3:(i+1)*3]
    slika, vrednost = karta[0], karta[1:]
    if vrednost in karte[slika]:
        print('GRESKA')
        sys.exit()

    karte[slika].add(vrednost)

print(*[13 - len(karte[k]) for k in ['P', 'K', 'H', 'T']])
