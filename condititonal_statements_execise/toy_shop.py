price_for_excursion = float(input())
number_of_puzzels = int(input())
number_of_speaking_doll = int(input())
number_of_teddy_bear = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

price_for_puzzel = 2.60
price_for_speaking_doll = 3
price_for_teddy_bear = 4.10
price_for_minions = 8.20
price_for_trucks = 2

all_toys = number_of_puzzels + number_of_speaking_doll + number_of_teddy_bear + number_of_minions + number_of_trucks
all_toys_price = (number_of_puzzels * price_for_puzzel) + (number_of_speaking_doll * price_for_speaking_doll) + (number_of_teddy_bear * price_for_teddy_bear) +(number_of_minions * price_for_minions) + (number_of_trucks * price_for_trucks)

if all_toys >= 50:
    discount = all_toys_price * 0.25
    total_price = all_toys_price - discount
else:
    total_price = all_toys_price
rent = total_price * 0.1
total_price = total_price - rent

if total_price >= price_for_excursion:
    left_over = total_price - price_for_excursion
    print(f"Yes! {left_over:.2f} lv left.")

if total_price < price_for_excursion:
    left_over = price_for_excursion - total_price
    print(f"Not enough money! {left_over:.2f} lv needed.")
