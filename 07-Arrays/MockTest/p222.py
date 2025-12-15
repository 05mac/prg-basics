def f(arr):
    a,b,c = arr[0],arr[1],arr[2]
    najczesciej = 0 
    if a == b:
        najczesciej = a
    elif a == c:
        najczesciej = a
    else:
        najczesciej = b
    if len(arr) < 3:
        return "error"
    
    for i in arr:
        if i != najczesciej:
            return i

print(f([7,7,7,7,7,5,7,7]))