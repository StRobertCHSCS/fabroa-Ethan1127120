number = int(input("Enter a number: "))

i = 0

while True:
    if 2**i > number:
        print(i-1)
        print((2**i)//2)
        break
    else:
        i += 1

