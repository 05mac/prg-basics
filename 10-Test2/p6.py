def f(years, course, average_grade):

    import json
    with open( "data.json", "r", encoding="utf-8") as file:
        content = json.load(file)
        
        licznik = 0
        print(content[0]['studies']["courses"])


        # for i in content:
        #     nazwa = i["studies"]["courses"] 
        #     wiek = i["age"]
        # #    srednia = sum(i["studies"]["courses"]) / len(i["studies"]["courses"])
        # #    if nazwa == course and years >= wiek and average_grade >= srednia:
        # #      licznik += 1

        #     if nazwa == "programming":
        #         print(i)




if __name__ == "__main__":
    print(f(21, "statistics", 4))