# 14. Exam Result Processing

# Goal: Store and analyze student exam results.
# Requirements:
# Store results as: (student_name, (subject1_score, subject2_score, ...))
# Calculate total and average using sum(), len().
# Use indexing to access specific subject.
# Tuple immutability ensures original scores aren't altered.


exam_results = [
    ("Alice", (85, 92, 78)),
    ("Bob", (88, 79, 94)),
    ("Charlie", (91, 85, 89)),
    ("David", (76, 84, 80)),
    ("Eve", (92, 95, 90))
]


def display_scores(exam_results):
    print("\n📊 Student Exam Scores")
    print("------------------------------")
    for name, scores in exam_results:
        total = sum(scores)
        average = total / len(scores)
        print(f"{name}: Total = {total}, Average = {average:.2f}")
    print("------------------------------")


def get_subject_score(exam_results, student_name, subject_index):
    for name, scores in exam_results:
        if name == student_name:
            try:
                return scores[subject_index]
            except IndexError:
                print(f"Error: Subject index {subject_index} out of range.")
                return None
    print(f"Error: Student '{student_name}' not found.")
    return None


display_scores(exam_results)


student_name = "Alice"
subject_index = 1  
score = get_subject_score(exam_results, student_name, subject_index)
if score is not None:
    print(f"\n{student_name}'s Subject {subject_index + 1} Score: {score}")
