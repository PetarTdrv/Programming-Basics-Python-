number = int(input())
even_sum = 0
odd_summ = 0

for i in range(number):
    current_number = int(input())
    if i % 2 == 0:
        even_sum += current_number
    else:
        odd_summ += current_number

difference = abs(even_sum - odd_summ)

if even_sum == odd_summ:
    print("Yes")
    print(f"Sum = {even_sum}")
elif even_sum != odd_summ:
    print("No")
    print(f"Diff = {difference}")
