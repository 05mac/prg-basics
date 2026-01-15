class C:
    def __init__(self, sectors):
        self.slownik = sectors

    def m1(self,s,n):
        self.slownik[s] = n
        return self.slownik

    def m2(self,s):
        liczba_fanow = 0
        s = s.upper()
        for i in s:
            if self.slownik.get(i):
                liczba_fanow += self.slownik[i]
        return liczba_fanow
if __name__ == "__main__":
    chleb = C({"A":120,"D":150,"G":90,"K":110})
    chleb.m1("G",130)
    print(chleb.m2("gd"))
    print(chleb.m2("KEJ"))
    