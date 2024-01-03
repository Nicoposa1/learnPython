file = open("text.txt", "r")
# print(file.read())
# print(file.readline())
for line in file:
    print(line)
file.close()

with open("text.txt", "r") as file: 
    for line in file: 
        print(line)
