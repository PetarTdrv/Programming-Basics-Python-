import math

count_of_numbers = int(input())
sum_of_all_elements = 0
max_element = -math.inf

for number in range(count_of_numbers):
    current_number = int(input())
    sum_of_all_elements += current_number
    if current_number > max_element:
        max_element = current_number
if max_element == sum_of_all_elements - max_element:
    print(f"Yes\nSum = {max_element}")
else:
    difference = abs(max_element - ( sum_of_all_elements - max_element))
    print(f"No\nDiff = {difference}")
