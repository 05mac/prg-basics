def f (first_letter, last_letter):

    with open("data.txt", "r", encoding="utf-8") as file:
        content = file.read()
        slowa = content.split()
        licznik = 0
        for slowo in slowa:
            if slowo.startswith(first_letter) and slowo.endswith(last_letter):
                licznik += 1
        
        
        return licznik


if __name__ == "__main__":

    print(f("w","d"))