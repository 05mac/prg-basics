def f(binary_number):
    binary_numbers = [1, 0]
    napis = len(binary_number)
    licznik = 0
    for i in binary_number:
        if int(i) in binary_numbers:
            licznik += 1
        elif int(i.isalpha()) == False:
            return False
    return licznik == napis


if __name__ == "__main__":
    print(f("101101"))
    print(f("131110100"))
