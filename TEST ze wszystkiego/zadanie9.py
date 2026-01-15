def f(sentence):
    samogloski = ["a","e","i","o","u","y"]
    licznik = 0
    sentence1 = sentence.lower()

    for i in sentence1:
        if str(i) in samogloski:
            licznik += 1
    return licznik

if __name__ == "__main__":
    print(f("water"))
    print(f("hello world"))
