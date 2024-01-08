from sys import maxsize

max_number = -maxsize

while True:
    text = input()
    if text == "Stop":
        break

    integer = int(text)

    if integer > max_number:
        max_number = integer

print(max_number)
