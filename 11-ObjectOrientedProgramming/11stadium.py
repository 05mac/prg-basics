class C:
    def __init__(self, slownik):
        self.slownik = slownik

    def m1(self, s, n):
        # wybiera zmienia liczbe fanow n w sekstorze s
        if self.slownik[s]:
            self.slownik[s] = n

    def _m2(self, s):
        licznik = 0

        for litera in s:
            licznik += self.slownik.get(litera, 0)

        return licznik


mecz1 = C({"A": 120, "D": 150, "G": 90, "K": 110})
mecz1.m1("G", 130)
print(mecz1._m2("GD"))
print(mecz1._m2("KEJ"))
