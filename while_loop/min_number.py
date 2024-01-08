from sys import maxsize

min_number = maxsize

while True:
    text = input()
    if text == "Stop":
        break

    integer = int(text)

    if integer < min_number:
        min_number = integer

print(min_number)
