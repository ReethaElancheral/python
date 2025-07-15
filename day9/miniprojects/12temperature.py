# 12. Daily Temperature Logger

# Goal: Track and analyze daily temperatures.
# Requirements:
# Store temperatures as (date, (morning_temp, evening_temp))
# Use slicing to get data for last 7 days.
# Find highest evening temperature using max().
# Use unpacking in analysis reports.


temperature_log = [
    ("2025-07-01", (35.5, 38.2)),
    ("2025-07-02", (34.0, 37.8)),
    ("2025-07-03", (33.5, 36.9)),
    ("2025-07-04", (36.0, 39.0)),
    ("2025-07-05", (35.8, 38.5)),
    ("2025-07-06", (34.2, 37.2)),
    ("2025-07-07", (33.8, 36.5)),
    ("2025-07-08", (34.5, 37.0)),
    ("2025-07-09", (35.0, 38.0)),
    ("2025-07-10", (36.3, 39.5))
]


def display_last_7_days(temperature_log):
    print("\n📅 Last 7 Days Temperature Log")
    print("-------------------------------")
    for date, (morning_temp, evening_temp) in temperature_log[-7:]:
        print(f"{date}: Morning: {morning_temp}°C, Evening: {evening_temp}°C")
    print("-------------------------------")


def highest_evening_temp(temperature_log):
    highest = max(temperature_log, key=lambda x: x[1][1])  
    date, (morning_temp, evening_temp) = highest
    print(f"\n🔥 Highest Evening Temperature: {evening_temp}°C on {date}")


display_last_7_days(temperature_log)


highest_evening_temp(temperature_log)
