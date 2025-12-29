def f(years, course, average_grade):

    import json
    with open( "data.json", "r", encoding="utf-8") as file:
        content = json.load(file)
        
        licznik = 0



        # SPOSOB 1
        for i in content:
            pierwszy_kurs = i["studies"]["courses"][0]

            if pierwszy_kurs["name"] == course:
                wiek = i["age"]
                oceny = pierwszy_kurs["grades"]
    
                if len(oceny) > 0:
                    srednia = sum(oceny) / len(oceny)

                    if wiek >= years and srednia >= average_grade:
                        licznik += 1
        return licznik




        # SPOSOB 2


        # for osoba in content:
        #     if osoba['age'] >= years:
        #         for kurs in osoba['studies']["courses"]:
        #             if kurs["name"] == course:
        #                 oceny = kurs["grades"]
        #                 srednia = sum(oceny) / len(oceny)

        #                 if srednia >= average_grade:
        #                     licznik += 1
        # return licznik

        
if __name__ == "__main__":
    print(f(21, "programming", 4))