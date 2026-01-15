def f(name):
    name = name.split()
    napis = ""
    for i in name:
        napis += i[0]
    return napis


if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python") )