needed_nylon = int(input())
needed_dye = int(input())
needed_thinner = int(input())
hours_for_masters = int(input())

# additional materials

additional_dye = (needed_dye * 0.10) + needed_dye
additional_nylon = needed_nylon + 2

total_price_for_nylon = additional_nylon * 1.50
total_price_for_dye = additional_dye * 14.50
total_price_for_thinner = needed_thinner * 5.00

total_sum = total_price_for_dye + total_price_for_nylon + total_price_for_thinner + 0.40

price_for_masters = (total_sum * 0.30) * hours_for_masters

full_price = total_sum + price_for_masters

print(f"{full_price:.2f}")
