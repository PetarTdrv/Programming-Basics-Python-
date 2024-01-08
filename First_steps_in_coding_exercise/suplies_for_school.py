number_of_pens = int(input())
number_of_markers = int(input())
liters_for_cleaning_table = int(input())
percent_discount = int(input())

full_price_for_pens = number_of_pens * 5.80
full_price_for_markers = number_of_markers * 7.20
full_price_for_chemichal = liters_for_cleaning_table * 1.20

full_price = full_price_for_pens + full_price_for_markers + full_price_for_chemichal

discount = percent_discount / 100

full_price_with_discount = full_price - (full_price * discount)

print(full_price_with_discount)
