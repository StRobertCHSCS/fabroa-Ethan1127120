number = int(input("Insert a number: "))

i = 2

while i >= 2:
    if (number/i) == float(number//i):
        print(i)
        break
    else:
        i += 1