###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    licznik = 0
    if number < 0:
        number = abs(number)
    number = str(number)

    for i in number:
        i = int(i)
        licznik += i
    return licznik


any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')
