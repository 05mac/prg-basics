with open("pets.txt", "r") as file:
    content = file.read()
    words_list = content.split(" ")
    print(len(words_list))