# 9. Grade Calculator with Recursive Input

# Use Case: Accept grades from user, retry until valid. 
# Exception Handling Goals:
# Use recursion inside try block
# Catch ValueError and retry
# Use finally to print final count of valid entries

valid_count = 0

def get_grade():
    global valid_count
    try:
        grade = input("Enter grade (A, B, C, D, F): ").upper()
        if grade not in ['A', 'B', 'C', 'D', 'F']:
            raise ValueError("Invalid grade entered.")
    except ValueError as ve:
        print(f"❌ {ve} Please try again.")
        get_grade()  # Recursive call to retry
    else:
        valid_count += 1
        print(f"✅ Grade '{grade}' accepted.")
    finally:
        print(f"📝 Valid entries so far: {valid_count}")

if __name__ == "__main__":
    num_grades = int(input("How many grades do you want to enter? "))
    for _ in range(num_grades):
        get_grade()
    print(f"\n🎉 Total valid grades entered: {valid_count}")
