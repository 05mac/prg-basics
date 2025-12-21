def f (arr):

    a = arr[0]
    b = arr[1]
    c = arr[2]
    powtarzajaca = 0

    if a == b:
        powtarzajaca = a
    
    if a == c:
        powtarzajaca = a

    if b == c:
        powtarzajaca = b

    for i in arr:
        if i != powtarzajaca:
            return i


if __name__ == "__main__":
    print(f([1,7,7,7,7,7,7,7]))