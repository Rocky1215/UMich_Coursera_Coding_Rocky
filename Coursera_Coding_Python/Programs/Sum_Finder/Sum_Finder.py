import re

name = input("Enter file:")
handle = open(name)
numbers = list()
for line in handle:
    x = line
    y = re.findall('([0-9]+)', x)
    if len(y) < 1:
        continue
    for i in y:
        iy = int(i)
        numbers.append(iy)
totsumnumbers = sum(numbers)

print(totsumnumbers)