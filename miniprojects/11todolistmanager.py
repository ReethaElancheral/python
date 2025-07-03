## 11. To-Do List Manager

# - Let the user add three tasks.
# - Store tasks in a list.
# - Print the list and each task with its number (index).

task1 = input("Enter task 1: ")
task2 = input("Enter task 2: ")
task3 = input("Enter task 3: ")

tasks = [task1, task2, task3]

print(*tasks, sep=",")

print("Task 1:", tasks[0])
print("Task 2:", tasks[1])
print("Task 3:", tasks[2])
