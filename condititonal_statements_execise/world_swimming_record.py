record_in_seconds = float(input())
distance_in_meters = float(input())
time_per_seconds_for_one_meter = float(input())

delay = (distance_in_meters // 15) * 12.5
total_time = (distance_in_meters * time_per_seconds_for_one_meter) + delay


if total_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    difference = total_time - record_in_seconds
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
