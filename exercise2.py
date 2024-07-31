# ----------------------------------------foreign time zone

from datetime import datetime
import pytz # type: ignore

# Define the foreign time zone (e.g., 'America/New_York')
foreign_timezone = pytz.timezone('America/New_York')

# Get the current time in the foreign time zone
foreign_time = datetime.now(foreign_timezone)

# Format the time to include AM/PM
formatted_time = foreign_time.strftime("%I:%M:%S %p")

# Determine the appropriate greeting based on the hour
hour = foreign_time.hour

if 5 <= hour < 12:
    greeting = "Good Morning"
elif 12 <= hour < 17:
    greeting = "Good Afternoon"
elif 17 <= hour < 21:
    greeting = "Good Evening"
else:
    greeting = "Good Night"

# Print the greeting and current time
print(f"{greeting}, the current time is {formatted_time} in the foreign time zone.")