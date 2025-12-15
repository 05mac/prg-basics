def f(subject):

    highest_average = 0
    best_subject_name = ""

    for subject_name, grade_list in subject.items():
        total_sum = sum(grade_list)
        count = len(grade_list)

        current_average = total_sum / count

        if current_average > highest_average:
            highest_average = current_average
            best_subject_name = subject_name
    return best_subject_name



print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))