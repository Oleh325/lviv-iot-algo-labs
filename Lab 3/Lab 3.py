employees = 0
beers = 0
compatibilityArray = []

with open("Lab 3/input.txt") as reader:
    employees, beers = reader.readline().split(" ")
    employees = int(employees)
    beers = int(beers)
    for compatibility in reader.readline().split(" "):
        compatibilityArray.append(compatibility)

