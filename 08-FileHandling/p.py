file = open("example.txt", "r")

content = file.read()


file.close

print(content)

############################

with open ('example.txt', 'r') as file:
    content = file(read)


