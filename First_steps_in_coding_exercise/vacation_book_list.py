number_of_page_book = int(input())
pages_per_one_hour = int(input())
number_of_days = int(input())

total_time_for_book = number_of_page_book / pages_per_one_hour
needed_time_per_day = total_time_for_book / number_of_days

print(f"{needed_time_per_day:.0f}")
