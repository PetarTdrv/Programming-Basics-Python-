number = int(input())

if 0 < number < 100:
    print('invalid')
elif 99 < number <= 200:
    pass
elif number > 200:
    print('invalid')
elif number < 0:
    print('invalid')
elif number == 0:
    exit()
