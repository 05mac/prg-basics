def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content



file_content = read_from_file("pets.txt")
file_lines = file_content.split()

# licznik = 0 
# for i in file_lines:
#     licznik += 1

print(len(file_lines))