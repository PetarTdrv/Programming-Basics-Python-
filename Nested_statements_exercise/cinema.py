type_of_projection = input()
rows = int(input())
colums = int(input())

income = 0
capacity = rows * colums

if type_of_projection == "Premiere":
    price = capacity * 12.00
elif type_of_projection == "Normal":
    price = capacity * 7.50
elif type_of_projection == "Discount":
    price = capacity * 5.00

print(f"{price:.2f}")
