# 7. Library Book 

# Goal: Maintain a catalog of books across multiple branches.
# Requirements:
# - Store each branch’s book list as a set.
# - Use union() to find all available books.
# - Use intersection() to find common books.
# - Use difference() to find books only in one branch.
# Concepts Covered: All set operations.


branch1 = {"1984", "To Kill a Mockingbird", "The Hobbit", "Dune"}
branch2 = {"Dune", "1984", "The Catcher in the Rye", "Fahrenheit 451"}
branch3 = {"The Hobbit", "Dune", "Brave New World", "1984"}

# 1. Union – all available books across branches
all_books = branch1.union(branch2, branch3)

# 2. Intersection – books common to all branches
common_books = branch1.intersection(branch2, branch3)

# 3. Difference – books unique to branch1
unique_branch1 = branch1.difference(branch2, branch3)


print("All books across branches:", all_books)
print("Books available in all branches:", common_books)
print("Books only in branch1:", unique_branch1)
