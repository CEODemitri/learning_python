file = open("csv_data.txt", "r")
lines = file.readlines()
file.close()

# retrieve all lines but the first
lines = [line.strip() for line in lines[1:]]

for line in lines:
    person = line.split(",")
    name = person[0].title()
    age = int(person[1])
    favorite = person[2]

    print(f'{name} is {age} and my favorite because {favorite}.')