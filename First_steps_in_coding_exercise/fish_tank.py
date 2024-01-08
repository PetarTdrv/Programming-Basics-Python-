lenght = int(input())
width = int(input())
height = int(input())
percent = float(input())

tank_volume = lenght * width * height
volume_liters = tank_volume * 0.001

geted_volume = percent / 100

needed_liters = volume_liters * (1 - geted_volume)
print(needed_liters)
