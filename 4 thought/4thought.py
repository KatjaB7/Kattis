odg  = { '256': '4 * 4 * 4 * 4', '0': '4 - 4 - 4 + 4','2': '4 / 4 + 4 / 4',
    '68': '4 + 4 * 4 * 4', '1': '4 - 4 + 4 / 4', '8': '4 - 4 + 4 + 4',
    '9': '4 + 4 + 4 / 4', '15': '4 * 4 - 4 / 4', '16': '4 - 4 + 4 * 4',
    '17': '4 / 4 + 4 * 4', '24': '4 + 4 + 4 * 4', '-60': '4 - 4 * 4 * 4',
    '32': '4 * 4 + 4 * 4', '60': '4 * 4 * 4 - 4', '7': '4 - 4 / 4 + 4',
    '-16': '4 - 4 - 4 * 4', '-15': '4 / 4 - 4 * 4', '-1': '4 - 4 - 4 / 4',
    '-8': '4 - 4 - 4 - 4', '-7': '4 / 4 - 4 - 4', '-4': '4 / 4 / 4 - 4',
    '4': '4 - 4 / 4 / 4', }

n = int(input())
for i in range(n):
    m = input()
    if m in odg:
        print('{} = {}'.format(odg[m], m))
    else:
    print('no solution') 