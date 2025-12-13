def f(array2D):
    suma_wiersza = [sum(wiersz) for wiersz in array2D]
    suma_kolumn = [sum(kolumna) for kolumna in zip(*array2D)]
    
    return suma_wiersza == suma_kolumn
        
array = [[3,7,2],
         [4,2,5],
         [5,2,1]
                ]
array2 = ([[3,7,2],[4,2,5],[9,2,1]])
print(f(array))
print(f(array2))
