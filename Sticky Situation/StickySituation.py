def pravilen_trikotnik(a, b, c):
    return a < b + c and b < a + c and c < a + b


input()
stranice = sorted(list(map(int, input().split())))
pravilen = False
for i in range(len(stranice) - 2):
    if pravilen_trikotnik(stranice[i], stranice[i + 1], stranice[i + 2]):
        pravilen = True
        break
if pravilen:
    print('possible')
else:
    print('impossible')
