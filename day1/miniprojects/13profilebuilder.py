## 13. Profile Builder

# - Ask for name, age, and city.
# - Store in a dictionary.
# - Print a formatted profile summary using f-strings.

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

profile = {
    "Name": name,
    "Age": age,
    "City": city
}


print(f"Profile Summary:Name: {profile['Name']}\nAge: {profile['Age']}\nCity: {profile['City']}")
