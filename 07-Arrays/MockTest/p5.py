def f(first_letter, last_letter):

    counter = 0
    with open("data.txt", "r", encoding="utf-8") as file:
        content = file.read()
        words = content.split()

        first = first_letter.lower()
        lastt = last_letter.lower()

        for word in words:
            if len(word) >= 1:

                current_word = word.lower()

                if current_word[0] == first and current_word[-1] == last:
                    counter += 1
    return counter


print(f("w", "d"))
