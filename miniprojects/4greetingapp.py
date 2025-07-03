## 4. Personal Greeting App

# - Ask the user for their name and favorite hobby.
# - Print a personalized greeting using f-strings.
# - Confirm the type of each input.

name = input("Enter Your name:")
hobby = input("Enter your fav hobby:")

print(f"Hello, {name}! It's great to know that you enjoy {hobby}.")

print("Type of name:", type(name))
print("Type of hobby:", type(hobby))
