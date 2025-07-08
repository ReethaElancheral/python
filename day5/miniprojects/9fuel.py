# ✅ 9. Fuel Filling Simulation

# Objective: Simulate filling fuel up to 50L.
# Requirements:
# Use while to repeatedly ask how much fuel to add.
# Accumulate total fuel.
# Use continue for zero or negative values.
# Stop when 50L is reached.

total_fuel = 0

while total_fuel < 50:
    amount = float(input("Enter amount of fuel to add (L): "))
    
    if amount <= 0:
        print("Invalid amount, please enter a positive value.")
        continue

    total_fuel += amount
    if total_fuel > 50:
        print(f"Fuel limit exceeded by {total_fuel - 50:.2f}L. Filling stopped.")
        break
    
    print(f"Total fuel filled: {total_fuel:.2f}L")

print("Fuel filling completed.")

