import math

name_of_serial = input()
time_of_one_episode = int(input())
time_of_break = int(input())

time_for_launch = time_of_break / 8.0
time_for_recreation = time_of_break / 4
time_left = time_of_break - (time_for_launch + time_for_recreation)

difference = abs(time_left - time_of_one_episode)

if time_left >= time_of_one_episode:
    print(f"You have enough time to watch {name_of_serial} and left with {math.ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_serial}, you need {math.ceil(difference)} more minutes.")
