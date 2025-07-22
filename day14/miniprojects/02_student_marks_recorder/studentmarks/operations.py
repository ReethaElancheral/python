import csv
import os

filename = "students.csv"

def add_student(name, roll, marks):
    try:
        marks = float(marks)
        if not os.path.exists(filename):
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Roll No", "Marks"])
        
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, roll, marks])
        print("Student data added.")
    except ValueError:
        print("❌ Please enter numeric marks.")

def view_records():
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            print("\n--- Student Records ---")
            for row in reader:
                print(", ".join(row))
    except FileNotFoundError:
        print("❌ students.csv not found!")

def show_summary():
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            total = 0
            count = 0
            topper = None
            top_marks = -1
            for row in reader:
                marks = float(row["Marks"])
                total += marks
                count += 1
                if marks > top_marks:
                    top_marks = marks
                    topper = row["Name"]

            if count > 0:
                average = total / count
                print(f"\n📊 Average Marks: {average:.2f}")
                print(f"🏆 Topper: {topper} with {top_marks} marks")
            else:
                print("No student records found.")
    except FileNotFoundError:
        print("❌ students.csv not found!")
