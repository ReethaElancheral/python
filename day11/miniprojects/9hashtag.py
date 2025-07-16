# 9. Hashtag Trend Tracker

# Goal: Track trending hashtags daily.
# Requirements:
# - Use daily sets of hashtags.
# - Combine all into a weekly trending set using update().
# - Find unique hashtags only used on one day.
# Concepts Covered: update(), symmetric_difference(), analysis.

# Daily hashtags captured from tweets or posts
day1 = {"#fun", "#python", "#news"}
day2 = {"#python", "#news", "#dev"}
day3 = {"#tech", "#fun", "#python"}

# 1. Combine all days into weekly trending set
weekly_trends = set()
weekly_trends.update(day1)
weekly_trends.update(day2)
weekly_trends.update(day3)
print("Weekly trends:", weekly_trends)

# 2. Find hashtags that appeared on exactly one day
unique_day1 = weekly_trends.copy()
for day in [day1, day2, day3]:
    unique_day1.symmetric_difference_update(day)
    
# unique_day1 now holds items seen exactly once
print("Hashtags used only one day:", unique_day1)
