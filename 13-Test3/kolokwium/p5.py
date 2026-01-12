def f(mnumbers):
    #liczby od 1 do 7
    #zawiera duze i male litery
    #zawiera plus i minus
    #na poczatku moze byc + lub -

    alfabet = "abcdABCD"
    nums = "12345"
    tablica = []
    for i in mnumbers:
        tablica.append(i)
    
    for i in tablica:
        for j in i:
            print(j)
           
            




if __name__ == "__main__":
    print(f(["A15","-31","7abC","+D1","-g4"]))