from sys import maxsize

max_number = -maxsize
min_number = maxsize
n = int(input())

for i in range(n):
    number = int(input())
    if number > max_number:
        max_number = number

    if number < min_number:
        min_number = number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
