# Sum of numbers

total = 0

number = int(input("Insert a number: "))

for i in range(number):
    total = (total + i) + 1

print(total)