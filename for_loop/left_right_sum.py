n = int(input())

left_sum = 0
right_sum = 0

for _ in range(n):
    number = int(input())
    left_sum += number

for _ in range(n):
    num = int(input())
    right_sum += num

difference = abs(left_sum - right_sum)
dif = str(difference)
right_su = str(right_sum)

if left_sum == right_sum:
    print("Yes, sum = " + right_su)
elif left_sum != right_sum:
    print("No, diff = " + dif)
