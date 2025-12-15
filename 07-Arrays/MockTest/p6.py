import json
def f (years,course_name,average_grade):

    count = 0
    with open ("data.json","r", encoding="utf-8") as file:
        dane = json.load(file)

    for dan in dane:
        if dan["age"] >= years:
            dane_courses = dan["studies"]["courses"]

            for course in dane_courses:
                if course["name"] == course_name:
                    grades = course["grades"]

                    if len(grades) > 0:
                                current_avg = sum(grades) / len(grades)

                                if current_avg >= average_grade:
                                    count += 1

                    break
    return count
print(f(20,"statistics",4))