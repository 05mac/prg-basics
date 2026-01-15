def f(word):
    word_index = 0
    string = ""
    if word == "":
        return ""
    
    wynik = []

    for i in range(len(word)):
        czesc = word[:i].lower() + word[i].upper() + word[i+1:].lower()
        wynik.append(czesc)
    
    return "-".join(wynik)


print(f("water"))