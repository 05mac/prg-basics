def f(d):
    suma = []
    for key,value in d.items():
        suma.append(value)
    counter = 0

    for key, value in d.items():
        if value > sum(suma) / len(suma):
            counter += 1
    return counter

        
if __name__ == "__main__":
    print(f({"LO231":150,"BA787":120,"NZ15":30}))
    print((f({"LO231":150,"BA787":20,"NZ15":30})))