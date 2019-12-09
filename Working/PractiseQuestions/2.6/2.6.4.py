start = int(input("Starting distance: "))
target = int(input("Target distance: "))

days = 1

while True:
    if start >= target:
        print("You will be ready to run" + str(target) + " km in: " + str(days))
        break
    else:
        (start) = start*1.1 
        days += 1