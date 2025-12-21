def f(subjects):
    srednia = 1
    najwyzsza_srednia = 1


    for subject, grades in subjects.items():
        srednia = (sum(grades) / len(grades))
        if srednia > najwyzsza_srednia:
            najwyzsza_srednia = srednia
    
    return subject


if __name__ == "__main__":
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))