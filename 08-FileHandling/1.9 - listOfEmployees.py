###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'
licznik = 0
with open("it_company.csv") as file:
   for line in file:
      if job_title in line:
         licznik += 1
         print(licznik)