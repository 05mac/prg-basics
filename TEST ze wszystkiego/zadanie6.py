#zdefiniuj funkcje f(number,even) ktora oblicza sume cyfr liczby
def f(number,even):
    suma_cyfr = 0
    for i in str(number):
        if even:
            if int(i) % 2 == 0:
                suma_cyfr += int(i)
        else:
            if int(i) % 2 != 0:
                suma_cyfr += int(i)
    return suma_cyfr
  

if __name__ == "__main__":
    print(f(3124,True))
    print(f(3124,False))
    print(f(20576,False))
    print(f(20576,True))
    print(f(13115,True))



