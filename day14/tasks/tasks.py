# Basic File Operations (1–10)

# 1.Create a new text file and write a welcome message.

with open("welcome.txt", "w") as file:
    file.write("Welcome to Python File Handling!")


# 2. Open a file, write multiple lines, and close it manually.

file = open("multilines.txt", "w")
file.write("Line 1: Hello!\n")
file.write("Line 2: This is a test.\n")
file.write("Line 3: File handling in Python.\n")
file.close()


# 3. Use the with statement to read a file without manually closing it.

with open("welcome.txt", "r") as file:
    content = file.read()
    print(content)


# 4. Read the contents of a file using .read().

with open("multilines.txt", "r") as file:
    print(file.read())


# 5. Read a file line-by-line using .readline().

with open("multilines.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()



# 6. Read all lines of a file into a list using .readlines().

with open("multilines.txt", "r") as file:
    lines = file.readlines()
    print(lines)  



# 7. Write a function that takes user input and appends it to a file.

# def append_user_input(filename):
#     user_input = input("Enter some text to append: ")
#     with open(filename, "a") as file:
#         file.write(user_input + "\n")

# append_user_input("user_notes.txt")


# 8. Write and overwrite a file using 'w' mode.

with open("overwrite.txt", "w") as file:
    file.write("This file has been overwritten.\n")



# 9. Append data to a file using 'a' mode and then display the full content.

with open("log.txt", "a") as file:
    file.write("Appended log entry.\n")

with open("log.txt", "r") as file:
    print(file.read())



# 10. Use 'x' mode to create a file, and handle the error if it already exists.

try:
    with open("newfile.txt", "x") as file:
        file.write("This file is newly created.")
except FileExistsError:
    print("File already exists!")


# Working with Context Managers & Modes (11–20)

# 11. Rewrite a script using with to ensure file auto-closing.

file = open("example.txt", "w")
file.write("Hello!")
file.close()

 #autoclose
with open("example.txt", "w") as file:
    file.write("Hello!")

# 12. Demonstrate reading and writing a binary file using 'wb' and 'rb'.

data = b"This is binary data."
with open("binaryfile.bin", "wb") as file:
    file.write(data)

with open("binaryfile.bin", "rb") as file:
    content = file.read()
    print(content)


# 13. Build a file reader that checks if a file is readable or writable.

with open("example.txt", "r+") as file:
    print("Readable:", file.readable())
    print("Writable:", file.writable())


# 14. Create a function that returns the number of words, lines, and characters in a file.

def file_stats(filename):
    with open(filename, "r") as file:
        text = file.read()
        lines = text.splitlines()
        words = text.split()
        return len(lines), len(words), len(text)

lines, words, chars = file_stats("user_notes.txt")
print(f"Lines: {lines}, Words: {words}, Characters: {chars}")


# 15. Create a report file that logs the time when a user logs in and out.

from datetime import datetime

def log_event(event):
    with open("report.txt", "a") as file:
        file.write(f"{event} at {datetime.now()}\n")

log_event("User login")
log_event("User logout")

# 16. Open a file and count how many times a specific word appears.

def count_word(filename, word):
    with open(filename, "r") as file:
        text = file.read()
        return text.lower().count(word.lower())

count = count_word("user_notes.txt", "yazh")
print(f"'yazh' appears {count} times.")


# 17. Replace a word in a file with another word and save the result.

def replace_word(filename, old, new):
    with open(filename, "r") as file:
        text = file.read()
    text = text.replace(old, new)
    with open(filename, "w") as file:
        file.write(text)

replace_word("example.txt", "Hello", "Hi")


# 18. Copy contents from one file to another file using file read and write.

with open("user_notes.txt", "r") as src, open("destination.txt", "w") as dst:
    dst.write(src.read())



# 19. Reverse the contents of a file line by line and save into a new file.

with open("user_notes.txt", "r") as src, open("reversed.txt", "w") as dst:
    for line in src:
        dst.write(line[::-1])


# 20. Write and read structured data using writelines() and readlines().

lines = ["Name: Reetha\n", "Location: Qatar\n", "Currency: INR\n"]

with open("structured.txt", "w") as file:
    file.writelines(lines)

with open("structured.txt", "r") as file:
    content = file.readlines()
    print(content)

# Error Handling & File Metadata (21–30)

# 21. Build a file handler that checks for FileNotFoundError and handles it.

try:
    with open("nonexistent.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found. Please check the filename.")



# 22. Display the file size and last modified date using os.path.

import os
import time

file_path = "example.txt"
if os.path.exists(file_path):
    size = os.path.getsize(file_path)
    modified = time.ctime(os.path.getmtime(file_path))
    print(f"Size: {size} bytes")
    print(f"Last Modified: {modified}")



# 23. Write a function that checks if a file exists and has write permission.

import os

def check_file_permissions(filepath):
    if os.path.exists(filepath):
        if os.access(filepath, os.W_OK):
            print("File exists and is writable.")
        else:
            print("File exists but is not writable.")
    else:
        print("File does not exist.")

check_file_permissions("example.txt")




# 24. Use try-except-finally to ensure a file is always closed after operations.

try:
    file = open("example.txt", "r")
    print(file.read())
except Exception as e:
    print("An error occurred:", e)
finally:
    file.close()
    print("File closed.")




# 25. Create a script that checks and prints the file extension of all files in a folder.

import os

folder = "."
for filename in os.listdir(folder):
    if os.path.isfile(os.path.join(folder, filename)):
        name, ext = os.path.splitext(filename)
        print(f"{filename} - Extension: {ext}")




# 26. Display all .txt files from a directory using os and glob.

import glob

txt_files = glob.glob("*.txt")
print("Text Files:", txt_files)



# 27. Rename a file and handle the case if the new name already exists.

import os

old_name = "example.txt"
new_name = "renamed.txt"

try:
    if os.path.exists(new_name):
        raise FileExistsError("Target file already exists.")
    os.rename(old_name, new_name)
    print("File renamed successfully.")
except FileExistsError as e:
    print(e)



# 28. Delete a file and handle PermissionError or FileNotFoundError.

try:
    os.remove("temp.txt")
    print("File deleted.")
except FileNotFoundError:
    print("File does not exist.")
except PermissionError:
    print("Permission denied to delete the file.")


# 29. Use os.makedirs() to create a folder structure for organizing files.

import os

folder_path = "project/reports/2025"
os.makedirs(folder_path, exist_ok=True)
print("Folder structure created.")



# 30. Move a file to another folder using shutil.

import shutil

shutil.move("renamed.txt", "project/reports/2025/renamed.txt")
print("File moved successfully.")


# CSV File Handling (31–35)

# 31. Create a CSV file containing student names and marks.

import csv

students = [
    ["Name", "Marks"],
    ["Anjali", 78],
    ["Reetha", 85],
    ["Priya", 92],
    ["Karan", 67]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)


# 32. Read the CSV file and print names of students who scored >80.

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    print("Students with marks > 80:")
    for row in reader:
        if int(row["Marks"]) > 80:
            print(row["Name"])



# 33. Append new student data to the CSV file.

new_student = ["Deepika", 88]

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_student)



# 34. Read a CSV and convert it into a dictionary of student names and marks.

student_dict = {}

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        student_dict[row["Name"]] = int(row["Marks"])

print(student_dict)


# 35. Create a report summarizing highest and average marks using a CSV file.

marks = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        marks.append(int(row["Marks"]))

highest = max(marks)
average = sum(marks) / len(marks)

print(f"Highest Marks: {highest}")
print(f"Average Marks: {average:.2f}")


# JSON File Handling (36–40)

# 36. Save user profile data (name, age, skills) into a .json file.

import json

profile = {
    "name": "Aarav",
    "age": 28,
    "skills": ["Python", "SQL", "Django"]
}

with open("profile.json", "w") as file:
    json.dump(profile, file, indent=4)



# 37. Read a .json file and display all user profiles.

with open("profile.json", "r") as file:
    data = json.load(file)
    print(data)


#38. Add a new entry into the existing .json data and save it back.

import json

new_profile = {
    "name": "Rekha",
    "age": 32,
    "skills": ["Java", "React"]
}

with open("profile.json", "r") as file:
    data = json.load(file)

# If it's a dict, convert to list
if isinstance(data, dict):
    profiles = [data]
elif isinstance(data, list):
    profiles = data
else:
    raise TypeError("Invalid JSON structure.")

# Append new profile
profiles.append(new_profile)

with open("profile.json", "w") as file:
    json.dump(profiles, file, indent=4)




# 39. Build a mini phonebook app using .json as the database.


import json
import os

def load_phonebook():
    if os.path.exists("phonebook.json"):
        with open("phonebook.json", "r") as file:
            return json.load(file)
    return {}

def save_phonebook(phonebook):
    with open("phonebook.json", "w") as file:
        json.dump(phonebook, file, indent=4)

def add_contact(name, number):
    phonebook = load_phonebook()
    phonebook[name] = number
    save_phonebook(phonebook)
    print("Contact saved.")

def view_contacts():
    phonebook = load_phonebook()
    for name, number in phonebook.items():
        print(f"{name}: {number}")


add_contact("Neha", "9876543210")
view_contacts()


# 40. Validate if a .json file contains required keys and handle errors.

import json

required_keys = {"name", "age", "skills"}

def validate_json(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise TypeError("Expected a list of profiles")

        for i, profile in enumerate(data, start=1):
            if not isinstance(profile, dict):
                raise ValueError(f"Profile #{i} is not a dictionary.")
            if not required_keys.issubset(profile.keys()):
                raise KeyError(f"Profile #{i} is missing required keys.")

        print("✅ All profiles are valid.")

    except (json.JSONDecodeError, TypeError, ValueError, KeyError) as e:
        print("❌ Invalid JSON:", e)

validate_json("profile.json")



# Log Files & Monitoring (41–45)

# 41. Build a simple logger that writes logs with timestamps to a file.

from datetime import datetime

def log_message(message):
    with open("app.log", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}\n")

log_message("Application started.")


# 42. Monitor a directory and write a log of any new file added (mock logic).

import os
import time

def monitor_directory(path, iterations=3):
    previous_files = set(os.listdir(path))
    for _ in range(iterations):
        current_files = set(os.listdir(path))
        new_files = current_files - previous_files
        for file in new_files:
            log_message(f"New file detected: {file}")
        previous_files = current_files
        time.sleep(5)


monitor_directory(".", iterations=2)



# 43. Track user login activity with date and time written to a log file.

from datetime import datetime

def log_user_login(username, logfile="user_login.log"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(logfile, "a") as file:
        file.write(f"[{timestamp}] User '{username}' logged in.\n")


log_user_login("admin_user")




# 44. Record program execution steps to a log file and allow log filtering.

def log_step(step, level="INFO"):
    with open("execution.log", "a") as file:
        file.write(f"[{level}] {step}\n")

def show_logs(level_filter=None):
    with open("execution.log", "r") as file:
        for line in file:
            if level_filter is None or f"[{level_filter}]" in line:
                print(line.strip())

log_step("Initializing system")
log_step("Loading configuration", "DEBUG")
log_step("Connection successful", "INFO")
show_logs("INFO")




# 45. Rotate log files daily and archive them by date.

import shutil
from datetime import datetime

def rotate_logs(log_filename="app.log"):
    if os.path.exists(log_filename):
        date_suffix = datetime.now().strftime("%Y-%m-%d")
        archive_name = f"logs/archive_{date_suffix}.log"
        os.makedirs("logs", exist_ok=True)
        shutil.move(log_filename, archive_name)
        print(f"Log rotated to {archive_name}")

rotate_logs()


# Text File Processing Projects (46–50)

# 46. Build a To-Do List app that saves tasks to a .txt file and retrieves them.

def add_task(task):
    with open("todo.txt", "a") as file:
        file.write(task + "\n")

def view_tasks():
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")


add_task("Finish file handling task")
view_tasks()



# 47. Create a program that merges two text files into one.

def merge_files(file1, file2, output_file):
    with open(file1, "r") as f1, open(file2, "r") as f2, open(output_file, "w") as fout:
        fout.write(f1.read())
        fout.write("\n")  # Optional: separate files
        fout.write(f2.read())

merge_files("user_notes.txt", "newfile.txt", "merged.txt")




# 48. Build a script that converts .txt to .pdf using file reading and a package like fpdf.

from fpdf import FPDF

def txt_to_pdf(input_file, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(input_file, "r") as file:
        for line in file:
            pdf.cell(200, 10, txt=line.strip(), ln=True)

    pdf.output(output_file)

txt_to_pdf("todo.txt", "todo.pdf")





# 49. Implement a file difference checker that compares two files line by line.

def compare_files(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    for i, (line1, line2) in enumerate(zip(lines1, lines2), 1):
        if line1 != line2:
            print(f"Line {i} differs:\n  File1: {line1.strip()}\n  File2: {line2.strip()}")

compare_files("user_notes.txt", "welcome.txt")



# 50. Write a program that saves a diary entry daily in a file named by date (e.g., 2025-07-02.txt).

from datetime import date

def save_diary_entry(entry):
    filename = date.today().strftime("%Y-%m-%d") + ".txt"
    with open(filename, "a") as file:
        file.write(entry + "\n")

save_diary_entry("Today I completed all 50 file handling tasks!")
