#1 Write a Python program to subtract five days from current date.
from datetime import datetime, timedelta

# Get the current date
current_date = datetime.today()

# Subtract 5 days
new_date = current_date - timedelta(days=5)

# Print the result
print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Date 5 days ago:", new_date.strftime("%Y-%m-%d"))


#2 Write a Python program to print yesterday, today, tomorrow.
from datetime import datetime, timedelta

# Get today's date
today = datetime.today()

# Calculate yesterday and tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

# Print the results
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))



#3 Write a Python program to drop microseconds from datetime.
from datetime import datetime

# Get the current datetime
current_datetime = datetime.now()

# Remove microseconds by setting them to 0
datetime_without_microseconds = current_datetime.replace(microsecond=0)

# Print the results
print("Original Datetime:", current_datetime)
print("Datetime without Microseconds:", datetime_without_microseconds)



#4 Write a Python program to calculate two date difference in seconds.
from datetime import datetime

# Define two dates
date1 = datetime(2024, 2, 10, 12, 30, 45)  # Example date and time
date2 = datetime(2024, 2, 15, 14, 45, 30)  # Another example date and time

# Calculate the difference in seconds
difference_in_seconds = abs((date2 - date1).total_seconds())

# Print the result
print("Difference in seconds:", difference_in_seconds)