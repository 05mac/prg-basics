import re
def f(array):
    pattern = r"^[a-z0-9_]{4,12}$"

    count = 0
    for i in array:
        if re.fullmatch(pattern, i):
            count += 1
    return count



if __name__ == "__main__":
    print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))