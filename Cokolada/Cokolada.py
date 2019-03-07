from math import log

K = int(input())
največje = 1
while največje < K:
    največje = največje*2

mn_kv = set()
naj = največje
k = K
while k > 0:
    if naj <= k:
        mn_kv.add(naj)
        k = k- naj
    naj //= 2

št_lom = int(log(največje, 2) - log(min(mn_kv), 2))
print(največje, št_lom)

