def f(subjects):
    najwyzsza_srednia = 1
    srednia = 1
    wspolrzedne = ""
    for key, value in subjects.items():
        srednia = (sum(value)) / (len(value))

        if srednia > najwyzsza_srednia:
            najwyzsza_srednia = srednia
            wspolrzedne = key
    return wspolrzedne


if __name__ == "__main__":
    print(f({"math": [3, 4, 4], "geo": [5, 4, 4, 4], "comp": [5, 4]}))
