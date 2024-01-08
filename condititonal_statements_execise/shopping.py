budget = float(input())
number_of_GPU = int(input()) # 250 
number_of_CPU = int(input()) # 35% of GPU price
number_of_RAM = int(input()) # 10% of GPU price

price_for_GPU = number_of_GPU * 250
price_for_CPU = number_of_CPU * (price_for_GPU * 0.35)
price_for_RAM = number_of_RAM * (price_for_GPU * 0.10)

full_price = price_for_GPU + price_for_CPU + price_for_RAM

if number_of_GPU > number_of_CPU:
    full_price = full_price * 0.85
    
difference = abs(full_price - budget)

if full_price <= budget:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
