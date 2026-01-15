def f(greeting):
    def f2(name):
        return f"{greeting}, {name}"

    return f2

if __name__ == "__main__":
    powitanie_pl = f("Cześć")
    print(powitanie_pl("Marek"))
