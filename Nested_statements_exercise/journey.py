budget = float(input())
season = input() #Winter or Summer

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        nights_in = "Camp"
        price = budget * 0.30
    elif season == "winter":
        nights_in = "Hotel"
        price = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        nights_in = "Camp"
        price = budget * 0.40
    elif season == "winter":
        nights_in = "Hotel"
        price = budget * 0.80
elif budget > 1000:
    nights_in = "Hotel"
    destination = "Europe"
    price = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{nights_in} - {price:.2f}")
