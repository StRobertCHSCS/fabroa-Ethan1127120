total = 0

for i in range(3):
    item_one = float(input("Enter item price: "))
    item_two = float(input("Enter quantity: "))
    total += item_one*item_two

final_price = total*1.13

print(round(final_price, 2))