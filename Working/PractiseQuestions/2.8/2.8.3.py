total = 0

number_one = int(input("Enter first number: "))

number_two = int(input("Enter second number: "))

for i in range(number_one,number_two+1):
    total = total + i

print(total)