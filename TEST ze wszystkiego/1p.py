# Reverse Polish Notation
def f(exppression):
    napis = []
    wynik = 0
    for i in exppression.split():
        if i != "+" and i != "-":
            napis.append(i)
        if i == "+":
            liczba1 = napis.pop()
            liczba2 = napis.pop()
            wynik = int(liczba1) + int(liczba2)
            napis.append(str(wynik))
        if i == "-":
            liczba1 = napis.pop()
            liczba2 = napis.pop()
            wynik = int(liczba2) - int(liczba1)
            napis.append(str(wynik))
    return int(napis[0])
   

if __name__ == "__main__":
    print(f("2 3 +"))
    print(f("2 6 + 4 5 - +"))
    print(f("11 7 + 15 - 14 +"))
