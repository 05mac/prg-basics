def f(car, order):
    slownik = {}
    wynik = []
    if order == 1:
        for vehicle in car:
            for register, km in vehicle.items():
                slownik[register] = km
        wynik.append(dict(sorted(slownik.items())))
    

    if order == 2:
        for vehicle in car:
            for register, km in vehicle.items():
                slownik[register] = km
        wynik.append(dict(sorted(slownik.items(), key=lambda item: item[1], reverse = True)))
    return wynik


if __name__ == "__main__":
    cars = [{"KR333":138},{"WL555":497},{"DB444":341},{"MC222":412}]
    print(f(cars,1))
    print(f(cars,2))