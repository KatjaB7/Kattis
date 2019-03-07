import sys

for vrst in sys.stdin:
    sez = (vrst.rstrip()).split()
    v =(sez[3]).split(':')
    z =(sez[4]).split(':')
    casV = int(v[0])*60 + int(v[1])
    casZ= int(z[0])*60 + int(z[1])
    s = casZ -casV
    print(sez[0],sez[1],sez[2], s//60, 'hours', s%60, 'minutes')
