# 13. Employee Shift Scheduler

# Goal: Schedule employee work shifts.
# Requirements:
# Store each shift as (employee_id, name, (start_time, end_time))
# Access specific timings using nested indexing.
# Use slicing to show first 5 employees.
# Iterate and unpack for payroll calculations.


shift_schedule = [
    (101, "Alice", ("09:00", "17:00")),
    (102, "Bob", ("10:00", "18:00")),
    (103, "Charlie", ("11:00", "19:00")),
    (104, "David", ("12:00", "20:00")),
    (105, "Eve", ("13:00", "21:00")),
    (106, "Frank", ("14:00", "22:00")),
    (107, "Grace", ("15:00", "23:00")),
    (108, "Hannah", ("16:00", "00:00"))
]


def display_first_5_shifts(schedule):
    print("\n🕒 First 5 Employees' Shifts")
    print("------------------------------")
    for _, name, (start_time, end_time) in schedule[:5]:
        print(f"{name}: {start_time} - {end_time}")
    print("------------------------------")


def calculate_payroll(schedule, hourly_rate):
    total_pay = 0
    print("\n💰 Payroll Calculation")
    print("------------------------------")
    for _, name, (start_time, end_time) in schedule:
        start_hour, start_minute = map(int, start_time.split(":"))
        end_hour, end_minute = map(int, end_time.split(":"))
       
        total_minutes = (end_hour - start_hour) * 60 + (end_minute - start_minute)
        total_hours = total_minutes / 60
        pay = total_hours * hourly_rate
        total_pay += pay
        print(f"{name}: {total_hours:.2f} hours → ${pay:.2f}")
    print("------------------------------")
    print(f"Total Payroll: ${total_pay:.2f}")


display_first_5_shifts(shift_schedule)


hourly_rate = 20  
calculate_payroll(shift_schedule, hourly_rate)
