###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0
additional_rinse = 15
additional_spin = 9

program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')

# logika wyboru progamu
if program == "j":
    total_washing_time = 40
elif program == "u":
    total_washing_time = 70
elif program == "s":
    total_washing_time = 20
else:
    print("Nie możemy obsłużyć twojego prania :/")
    exit()
    

if extra_rinse == "y":
    total_washing_time += additional_rinse
    
if extra_spin == "y":
    total_washing_time += additional_spin

if total_washing_time > 0:
    print(f"Total washing time: {total_washing_time} minutes")
else:
    print("Brak czasu prania (błędny program).")
