
VALID_SHIFTS = {"Morning", "Evening", "Night"}

def assign_shift(shift_registry, employee_id, name, shift):
    if shift not in VALID_SHIFTS:
        print(f"Invalid shift '{shift}'. Valid options: {VALID_SHIFTS}")
        return
    
  
    existing_shifts = {info["shift"] for info in shift_registry.values()}
    if shift in existing_shifts:
        print(f"Shift '{shift}' already assigned to another employee.")
        return

    shift_registry[employee_id] = {
        "name": name,
        "shift": shift
    }
    print(f"Assigned {name} (ID: {employee_id}) to {shift} shift.")

def display_shifts(shift_registry):
    if not shift_registry:
        print("No shifts assigned yet.")
        return
    print("\n--- Current Shift Assignments ---")
    for emp_id, info in shift_registry.items():
        print(f"ID: {emp_id}, Name: {info['name']}, Shift: {info['shift']}")
