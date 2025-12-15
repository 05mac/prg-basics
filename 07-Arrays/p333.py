def f (array2D):
    wiersz = [sum(wiersz) for wiersz in array2D]
    kolumna = [sum(kolumna) for kolumna in zip(*array2D)]
    
    return wiersz == kolumna

print(f([[3,7,2],[4,2,5],[5,2,1]]))
print(f([[3,7,2],[4,2,5],[9,2,1]]))