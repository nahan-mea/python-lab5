from datetime import datetime, timedelta

today = datetime.today()
print("Yesterday:", (today - timedelta(1)).date())
print("Today:", today.date())
print("Tomorrow:", (today + timedelta(1)).date())
