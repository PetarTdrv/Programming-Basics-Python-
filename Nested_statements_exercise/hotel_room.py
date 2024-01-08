month = input()
nights = int(input())
full_price_for_studio = 0
full_price_for_apartment = 0

if month == "May" or month == "October":
    if 14 >= nights >= 7:
        studio_price = 50
        apartment_price = 65
        total_price_for_studio = nights * studio_price
        full_price_for_studio = total_price_for_studio * 0.95
        full_price_for_apartment = nights * apartment_price
    elif nights > 14:
        studio_price = 50
        apartment_price = 65
        total_price_for_studio = nights * studio_price
        full_price_for_studio = total_price_for_studio * 0.70
        total_price_for_apartment = nights * apartment_price
        full_price_for_apartment = total_price_for_apartment * 0.90
elif month == "June" or month == "September":
    if nights > 14:
        studio_price = 75.20
        apartment_price = 68.70
        total_price_for_studio = nights * studio_price
        full_price_for_studio = total_price_for_studio * 0.80
        total_price_for_apartment = nights * apartment_price
        full_price_for_apartment = total_price_for_apartment * 0.90
    elif nights <= 14:
            studio_price = 75.20
            apartment_price = 68.70
            total_price_for_studio = nights * studio_price
            full_price_for_studio = total_price_for_studio 
            total_price_for_apartment = nights * apartment_price
            full_price_for_apartment = total_price_for_apartment
elif month == 'July' or month == "August":
    if nights > 14:
        studio_price = 76
        apartment_price = 77
        total_price_for_studio = nights  * studio_price
        full_price_for_studio = total_price_for_studio
        total_price_for_apartment = nights * apartment_price
        full_price_for_apartment = total_price_for_apartment * 0.9
    elif nights <= 14:
        studio_price = 76
        apartment_price = 77
        total_price_for_studio = nights  * studio_price
        full_price_for_studio = total_price_for_studio
        total_price_for_apartment = nights * apartment_price
        full_price_for_apartment = total_price_for_apartment

print(f"Apartment: {full_price_for_apartment:.2f} lv.")
print(f"Studio: {full_price_for_studio:.2f} lv.")
