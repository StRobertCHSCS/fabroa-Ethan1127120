total = 0

number_one = int(input("Enter first number: "))

number_two = int(input("Enter second number: "))

if number_one <= number_two:
    for i in range(number_one, number_two+1):
        print(i)
else:
    for i in range(number_one, number_two-1,-1):
        print(i)