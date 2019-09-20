students = int(input("Enter the number of students: "))
apples = int(input("Enter the number of apples: "))

print("Each student gets " + str(apples//students))
print("There is a remainder of " + str(apples % students) + " apples")
