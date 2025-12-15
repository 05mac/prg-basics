tablica = [1,6,7,8,2,3,5,6,7,2]


def sortowanie_babelkowe (tablica):

    def swap (tablica, dx1, dx2):
        tablica[dx1], tablica[dx2] = tablica[dx2], tablica[dx1]

    n = len(tablica)
    for i in range(n-1):
        for j in range(n-i-1):
            if tablica[j] > tablica[j+1]:
                swap(tablica,j,j+1)
    return tablica

print(sortowanie_babelkowe(tablica))