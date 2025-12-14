def f(player1, player2):
    A = 10
    K = 10
    Q = 10
    J = 10
    T = 10
    special_card = ["A", "K", "Q", "J", "T"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    suma_player1 = 0
    suma_player2 = 0

    for i in player1:
        if i in special_card:
            suma_player1 += 10
        elif i in numbers:
            suma_player1 += int(i)
    

    for i in player2:
        if i in special_card:
            suma_player2 += 10
        elif i in numbers:
            suma_player2 += int(i)
    
    if suma_player1 >= suma_player2:
        return True
    else:
        return False

print(f("AJ972", "AQT72"))
print(f("9532", "K8"))

