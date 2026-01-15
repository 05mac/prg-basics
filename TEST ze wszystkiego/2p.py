def f(array2D):
    suma_wierszy = [sum(suma_wierszy) for suma_wierszy in array2D]
    suma_kolumn = [sum(suma_kolumn) for suma_kolumn in zip(*array2D)]

    return suma_wierszy == suma_kolumn
    

if __name__ == "__main__":
    print(f([[3,7,2], [4,2,5], [5,2,1]]))