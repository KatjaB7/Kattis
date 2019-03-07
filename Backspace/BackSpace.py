vrstica = input()
ven = [''] * len(vrstica)
št = 0
for znak in vrstica:
    if znak == '<':
        št -= 1
        ven[št] = ''
    else:
        ven[št] = znak
        št += 1
print(''.join(ven))
