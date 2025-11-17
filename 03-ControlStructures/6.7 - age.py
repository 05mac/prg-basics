
age = int(input("Podaj swój wiek: "))

if age < 13:
    print("jestes dzieckiem")
elif age in (13, 19):
    print("jestes nastolatkiem")
elif age in (20,64):
    print("jestes doroslym czlowiekem")
else:
    print("jestes seniorem")    