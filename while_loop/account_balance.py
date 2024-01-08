acount_balance = 0

while True:
    text = input()

    if text == "NoMoreMoney":
        break

    current_deposit_sum = float(text)

    if current_deposit_sum >= 0:
        acount_balance += current_deposit_sum
        print(f"Increase: {current_deposit_sum:.2f}")
    elif current_deposit_sum < 0:
        print("Invalid operation!")
        break

print(f"Total: {acount_balance:.2f}")
