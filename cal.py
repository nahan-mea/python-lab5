from datetime import datetime

now = datetime.now()

print("Current date and time:", now)
print("Current Year:", now.year)
print("Month of the year:", now.month)
print("Week number of the year:", now.isocalendar()[1])
print("Weekday of the week:", now.strftime("%A"))
print("Day of the year:", now.timetuple().tm_yday)
print("Day of the month:", now.day)
print("Day of the week (0=Monday, 6=Sunday):", now.weekday())
