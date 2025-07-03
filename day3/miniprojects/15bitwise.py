# 15. Bitwise Access Rights Checker


# Objective: Check permission using bitwise flags.
# Requirements:
# Use:
# 1: Read
# 2: Write
# 4: Execute
# Combine permissions using bitwise OR |, check using AND &.

READ = 1      # 0b001
WRITE = 2     # 0b010
EXECUTE = 4   # 0b100

perm = int(input("Enter permission value (0-7): "))


can_read = (perm & READ) != 0
can_write = (perm & WRITE) != 0
can_execute = (perm & EXECUTE) != 0

print(f"\nPermissions for value {perm}:")
print(f"Read Permission: {'Yes' if can_read else 'No'}")
print(f"Write Permission: {'Yes' if can_write else 'No'}")
print(f"Execute Permission: {'Yes' if can_execute else 'No'}")
