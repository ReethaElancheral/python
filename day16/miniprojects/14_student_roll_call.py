# 14. Student Roll-Call 

# Goal: Read student names and roll numbers one-by-one using iterator protocol. 
# Requirements: 
#  Create a dictionary {roll: name} 
#  Use iterator to display (roll, name) 
#  End when list is exhausted 

class RollCallIterator:
    def __init__(self, student_dict):
        self.entries = list(student_dict.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.entries):
            raise StopIteration
        entry = self.entries[self.index]
        self.index += 1
        return entry


students = {
    101: "Ravi",
    102: "Priya",
    103: "Amit"
}
print("Roll Call:")
for roll, name in RollCallIterator(students):
    print(f"Roll No: {roll}, Name: {name}")
