product = input()
day = input()
quantity = float(input())

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day ==  'Thursday' or day == 'Friday':
    if product ==  'banana':
        price = quantity * 2.50
    elif product == 'apple':
        price = quantity * 1.20
    elif product == 'orange':
        price = quantity * 0.85
    elif product == 'grapefruit':
        price = quantity * 1.45
    elif product == 'kiwi':
        price = quantity * 2.70
    elif product == 'pineapple':
        price = quantity * 5.50
    elif product == 'grapes':
        price = quantity * 3.85
elif day == 'Saturday' or day == 'Sunday':
    if product ==  'banana':
        price = quantity * 2.70
    elif product == 'apple':
        price = quantity * 1.25
    elif product == 'orange':
        price = quantity * 0.90
    elif product == 'grapefruit':
        price = quantity * 1.60
    elif product == 'kiwi':
        price = quantity * 3.00
    elif product == 'pineapple':
        price = quantity * 5.60
    elif product == 'grapes':
        price = quantity * 4.20
elif day != 'Monday' or day != 'Tuesday' or day != 'Wednesday' or day !=  'Thursday' or day != 'Friday':
    if product != 'banana' or product != 'apple' or product != 'orange' or product != 'grapefruit' != 'kiwi' or \
        product != 'pineapple' or product != 'grapes':
        print("error")

print(f"{price:.2f}")
