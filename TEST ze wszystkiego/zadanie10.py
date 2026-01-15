def f (array):
    smallest = array[0][0]
    for i in array:
        for j in i:
            if j <= smallest:
                smallest = j   
    return smallest


if __name__ == "__main__":
    print(f([[7,8],[5,3],[9,4]]))