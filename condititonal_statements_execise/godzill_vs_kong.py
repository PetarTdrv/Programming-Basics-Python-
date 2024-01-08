budget_for_movie = float(input())
number_of_statist = int(input())
price_for_dress_by_one_statist = float(input())

decor_price = budget_for_movie * 0.1
price_for_statist = number_of_statist * price_for_dress_by_one_statist

if number_of_statist > 150:
    price_for_statist = price_for_statist * 0.9

total_price = decor_price + price_for_statist
difference = abs(budget_for_movie - total_price)

if total_price > budget_for_movie:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
