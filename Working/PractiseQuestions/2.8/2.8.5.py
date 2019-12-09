total = 0

number_one = int(input("Input first number: "))

number_two = int(input("Input second number: "))

for i in range(number_one,number_two + 1):
    print(i)

total = 0

for i in range(number_one, number_two + 1):
    total = total + i

print(total)