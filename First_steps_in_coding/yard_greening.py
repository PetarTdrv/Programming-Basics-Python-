square_meter = int(input())

full_price = square_meter * 7.61

discount= full_price * 0.18

discount_ = full_price - discount
full_price = full_price - discount

print(f"The final price is: {full_price} lv.")
print(f"The discount is: {discount} lv.")
