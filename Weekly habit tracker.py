habit_info = ("Exercise","Read","Sleep early",30)
weekly_records = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
total_days=len(weekly_records)
first_day=weekly_records[0]
print("First day of the week:", first_day)
weekdays=weekly_records[0:5]
print("Weekdays:", weekdays)
extra_day=("Next Mon",)
updated_records=weekly_records+extra_day
print("Updated weekly records:", updated_records)
