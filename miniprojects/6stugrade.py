## 6. Student Gradebook

# - Ask for a student's name and three subject scores (input).
# - Store data in a dictionary.
# - Calculate the average and display results using f-strings.
# - Show type of the average.


name = input("Enter student's name: ")
score1 = float(input("Enter score for Subject 1: "))
score2 = float(input("Enter score for Subject 2: "))
score3 = float(input("Enter score for Subject 3: "))


gradebook = {
    "Name": name,
    "Subject 1": score1,
    "Subject 2": score2,
    "Subject 3": score3
}


average = (score1 + score2 + score3) / 3


print(f"\nStudent: {gradebook['Name']}")
print(f"Scores: {gradebook['Subject 1']}, {gradebook['Subject 2']}, {gradebook['Subject 3']}")
print(f"Average Score: {average:.2f}")


print("Type of average:", type(average))
