name_of_actor = input()
academy_points = float(input())
number_of_assessors = int(input())
total_points = 0
total_points += academy_points

for name_of_assesors in range(number_of_assessors):
    name_of_assesors = input()
    points_of_assesor = float(input())
    lenght = len(name_of_assesors)
    total_points = total_points + ((lenght * points_of_assesor) / 2)

needed_points = abs(1250.5 - total_points)
if total_points >= 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
elif total_points < 1250.5:
    print(f"Sorry, {name_of_actor} you need {needed_points:.1f} more!")
