# write a program which remind you of drinking water every hour or two. your program can either beep or 
# send desktop notification for specific operating system.

import time
from plyer import notification

def remind_to_drink_water(interval_hours):
    interval_seconds = interval_hours * 3600
    while True:
        notification.notify(
            title="Hydration Reminder",
            message="It's time to drink some water! Stay hydrated!",
            app_name="Water Reminder",
            timeout=10  # Notification will stay on screen for 10 seconds
        )
        time.sleep(interval_seconds)

if __name__ == "__main__":
    try:
        # Set the interval in hours (e.g., 1 for every hour, 2 for every 2 hours)
        interval = 1  # Change this value as needed
        print(f"Starting water reminder every {interval} hour(s). Press Ctrl+C to stop.")
        remind_to_drink_water(interval)
    except KeyboardInterrupt:
        print("\nWater reminder stopped. Stay hydrated!")
