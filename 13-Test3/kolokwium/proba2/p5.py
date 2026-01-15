import re
def f(mnumbers):
    pattern = r"^[+-]?[a-dA-D1-7]+$"

    count = 0
    for username in mnumbers:
        if re.findall(pattern, username): #
            count += 1
    return count


if __name__ == "__main__":
    print(f(["A15","-31","7abC","+D1","-g4"]))
    print(f(["A05","-3+1","7ab8C","+Bb7","-22c55"]))