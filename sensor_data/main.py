# 🧠 PART 2 — NOW LET’S LEARN THE CODING (STEP-BY-STEP)
# ✅ STEP 1: Simulate Sensor Data (Slides 13 & 17)
import random
import time

for i in range(10):
    temp_c = 25 + random.uniform(-2, 2)
    print(f"Reading {i+1}: {temp_c:.2f} °C")
    time.sleep(1)


# 🔹 random.uniform() → noise
# 🔹 sleep() → sampling rate

# ✅ STEP 2: Save Sensor Data to CSV
import random
import time
import csv

with open("sensor_readings.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "temp_c"])

    for i in range(20):
        ts = time.time()
        temp_c = 25 + random.uniform(-2, 2)
        writer.writerow([ts, f"{temp_c:.2f}"])
        time.sleep(0.5)


# 📌 CSV = sensor log file

# ✅ STEP 3: Visualize Raw Sensor Data
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sensor_readings.csv")

df["timestamp"] = pd.to_numeric(df["timestamp"], errors="coerce")
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

plt.plot(df["timestamp"], df["temp_c"])
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Raw sensor values")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ✅ STEP 4: Smooth Sensor Data (Noise Reduction)
df["value"] = pd.to_numeric(df["temp_c"], errors="coerce")
df["value_smooth"] = df["value"].rolling(window=5, min_periods=1).mean()

plt.plot(df["timestamp"], df["value"], label="Raw", alpha=0.5)
plt.plot(df["timestamp"], df["value_smooth"], label="Smoothed")
plt.legend()
plt.show()

# ✅ STEP 5: Interpret Trend (Slide 23)
mid_index = len(df) // 2

first_half_mean = df["value_smooth"].iloc[:mid_index].mean()
second_half_mean = df["value_smooth"].iloc[mid_index:].mean()

if second_half_mean > first_half_mean:
    print("Temperature increased")
elif second_half_mean < first_half_mean:
    print("Temperature decreased")
else:
    print("Temperature stable")



'''
🧠 MCQ LOCK — REMEMBER THESE 10 RULES

1️⃣ Sensor converts physical → data
2️⃣ Unit gives meaning to number
3️⃣ Sampling rate = how often
4️⃣ Resolution = smallest detectable change
5️⃣ Noise ≠ real change
6️⃣ Rolling mean reduces noise
7️⃣ Analog = continuous
8️⃣ Digital = discrete
9️⃣ CSV stores sensor logs
🔟 Trend detection via mean comparison
'''