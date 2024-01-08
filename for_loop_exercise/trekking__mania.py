number_of_groups = int(input())
mousalla_climbers = 0
monblan_climbers = 0
kilimandjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
total_climbers = 0

for current_group in range(number_of_groups):
    current_group_climbers = int(input())
    if current_group_climbers <= 5:
        mousalla_climbers += current_group_climbers
    elif current_group_climbers <= 12:
        monblan_climbers += current_group_climbers
    elif current_group_climbers <= 25:
        kilimandjaro_climbers += current_group_climbers
    elif current_group_climbers <= 40:
        k2_climbers += current_group_climbers
    elif current_group_climbers >= 41:
        everest_climbers += current_group_climbers
    total_climbers += current_group_climbers

percentage_mousalla_climbers = mousalla_climbers / total_climbers * 100
percentage_monblan_climbers = monblan_climbers / total_climbers * 100
percentage_kilimandjaro_climbers = kilimandjaro_climbers / total_climbers * 100
percentage_k2_climbers = k2_climbers / total_climbers * 100
percentage_everest_climbers = everest_climbers / total_climbers * 100

print(f"{percentage_mousalla_climbers:.2f}%")
print(f"{percentage_monblan_climbers:.2f}%")
print(f"{percentage_kilimandjaro_climbers:.2f}%")
print(f"{percentage_k2_climbers:.2f}%")
print(f"{percentage_everest_climbers:.2f}%")
