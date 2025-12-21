def f (player1, player2):
    cards = {"A": 10, "K": 10,"Q": 10,"J": 10,"T": 10, "9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2,"1":1}
    
    suma_kart_player1 = 0
    suma_kart_player2 = 0

    for i in player1:
        if i in cards:
            suma_kart_player1 += cards[i]

    for i in player2:
        if i in cards:
            suma_kart_player2 += cards[i] 


    return suma_kart_player1 > suma_kart_player2
if __name__ == "__main__":
    print(f("AJ972","AQT72"))
    print(f("9532","K8"))