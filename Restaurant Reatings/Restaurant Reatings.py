from functools import lru_cache

@lru_cache(maxsize=None)
def stevilo_nacinov(najvisja_ocena, st_kritikov):
    if st_kritikov == 0:
        return 1
    else:
        return sum(stevilo_nacinov(najvisja_ocena - i, st_kritikov - 1) for i in range(0, najvisja_ocena + 1))

def slaba_ocena(seznam_ocen):
    if len(seznam_ocen) == 0:
        return 1
    vsota = sum(seznam_ocen)
    koliko_moznosti = 0
    # primer 1: slabši prvi kritik
    for ocena in range(0, seznam_ocen[0]):
        koliko_moznosti += stevilo_nacinov(vsota - ocena, len(seznam_ocen) - 1)
    # primer 2: isti prvi kritik
    koliko_moznosti += slaba_ocena(seznam_ocen[1:])
    # primer 3: boljši prvi kritik
    for ocena in range(seznam_ocen[0] + 1, vsota):
        koliko_moznosti += stevilo_nacinov(vsota - ocena - 1, len(seznam_ocen) - 1)
    return koliko_moznosti

while True:
    seznam_ocen = list(map(int, input().split()))
    if seznam_ocen[0]== 0:
        break
    else:
        print(slaba_ocena(seznam_ocen[1:]))
