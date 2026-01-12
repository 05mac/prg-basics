def f(word):
    index_1 = 0

    return_string = ""
    word = word.lower()

    for turn in word:
        word_ = word
        word_ = word_[:index_1] + word_[index_1].upper() + word_[index_1+1:]


        if(index_1 ==len(word) - 1):
            return_string += word_
        else:
            return_string += word_ + "-"
        
        index_1 += 1


    return return_string

print(f("water"))