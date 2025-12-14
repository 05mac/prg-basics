def f(arr):
    a,b,c = arr[0], arr[1], arr[2]

    if a == b:
        wartosc_dominujaca = a
    elif a ==b:
        wartosc_dominujaca = a
    else:
        wartosc_dominujaca = b
    
    for i in arr:
        if i != wartosc_dominujaca:
            return i



print(f([7,7,7,7,0,7,7,7]))