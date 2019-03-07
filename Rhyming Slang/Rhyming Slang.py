class rime:
    def __init__(self):
        self.mn_rim = []

    def dodaj_rimo(self, l):
        self.mn_rim.append(l)

    def predpona(self, l, m):
        for bes in l:
            if m.endswith(bes):
                return True
        return False

    def preveri_rimo(self, a, b):
        for rima in self.mn_rim:
            if self.predpona(rima, a) and self.predpona(rima, b):
                return True
        return False

def main():
    beseda = input()
    mn_r = int(input())
    uredi = rime()
    for i in range(mn_r):
        uredi.dodaj_rimo(input().split())
    m = int(input())
    for m in range(m):
        if uredi.preveri_rimo(beseda, input()):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()

