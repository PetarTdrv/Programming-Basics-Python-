product = input()
city = input()
capacity = float(input())

if city == "Sofia":
    if product == "coffee":
        price = capacity * 0.50
    elif product == "water":
        price = capacity * 0.80
    elif product == "beer":
        price = capacity * 1.20
    elif product == "sweets":
        price = capacity * 1.45
    elif product == "peanuts":
        price = capacity * 1.60
elif city == "Plovdiv":
    if product == "coffee":
        price = capacity * 0.40
    elif product == "water":
        price = capacity * 0.70
    elif product == "beer":
        price = capacity * 1.15
    elif product == "sweets":
        price = capacity * 1.30
    elif product == "peanuts":
        price = capacity * 1.50
elif city == "Varna":
    if product == "coffee":
        price = capacity * 0.45
    elif product == "water":
        price = capacity * 0.70
    elif product == "beer":
        price = capacity * 1.10
    elif product == "sweets":
        price = capacity * 1.35
    elif product == "peanuts":
        price = capacity * 1.55
    
print(price)
