import re


def f(mnumbers):
    # liczby od 1 do 7
    # zawiera duze i male litery
    # zawiera plus i minus
    # na poczatku moze byc + lub -
    #     p5.py) A valid number on the planet Metis consists of the digits 1 through 7 and the lower or upper case letters a
    # through d. A plus (+) or minus (-) sign can also appear at the beginning of the number. Create a function
    # f(mnumbers) that returns how many numbers in the array mnumbers are valid on the planet Metis. Example:
    # f(["A15","-31","7abC","+D1","-g4"]) returns 4
    # f(["A05","-3+1","7ab8C","+Bb7","-22c55"]) returns 2

    pattern = r"^[+-]?[a-dA-D1-7]+$"
    count = 0
    for i in mnumbers:
        if re.findall(pattern, i):
            count += 1
    return count


if __name__ == "__main__":
    print(f(["A15", "-31", "7abC", "+D1", "-g4"]))
    print(f((["A05","-3+1","7ab8C","+Bb7","-22c55"])))
