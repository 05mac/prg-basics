  
for liczby in range(1,31):
    if (liczby % 3 == 0) and (liczby % 5 == 0):
        print(f"BINGO", end=" ")
    elif liczby % 3 == 0:
       print(f"THREE", end=" ")
    elif liczby % 5 == 0:
       print(f"FIVE", end=" ")
    else:
        print(f"{liczby}", end=" ")
