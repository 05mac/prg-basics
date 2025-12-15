
cards = {
    "A" : 10,"K" : 10,"Q" : 10,"J" : 10,"T" : 10,

}

def f(player1,player2):
    suma_player1 = 0
    suma_player2 = 0

    for element in player1:
        if element in cards:
            suma_player1 += cards[element]
        elif int(element) in range(1,10):
            suma_player1 += int(element)

    for element in player2:
        if element in cards:
            suma_player2 += cards[element]
        elif int(element) in range(1,10):
            suma_player2 += int(element)

    return suma_player1 >= suma_player2

if __name__ == "__main__": 
    print(f("AJ972","AQT72"))
    print(f("9532","K8"))