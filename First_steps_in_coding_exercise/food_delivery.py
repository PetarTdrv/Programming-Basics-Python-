number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegan_menus = int(input())

total_sum_for_chicken_menu = number_of_chicken_menus * 10.35
total_sum_for_fish_menu = number_of_fish_menus  * 12.40
total_sum_for_vegan_menu = number_of_vegan_menus * 8.15

total_sum = total_sum_for_chicken_menu + total_sum_for_fish_menu + total_sum_for_vegan_menu

dessert_price = total_sum * 0.20

full_price = total_sum + dessert_price + 2.50
print(round(full_price, 2))
