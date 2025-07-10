# 🟦 SECTION 1: Creating and Accessing Strings (1–10)

# ✅1. Create a string using single quotes, double quotes, and triple quotes.

str1 = 'Hi'
str2 = "hello"
str3 = ''' how are you?'''
print(str1,str2,str3)


# ✅2. Create a multiline quote using triple quotes and print it.

multi_line_quote = """This is a multiline
string using triple quotes.
It spans multiple lines."""
print(multi_line_quote)

# ✅3. Access the first and last characters from a string using positive and negative indexing.
string_access = "python"
print(string_access[0])
print(string_access[-1])


# ✅4. Write a program to print every character in a string using a for loop.
for char in string_access:
    print(char, end=' ')
print()


# ✅5. Slice a string to extract only the middle 3 characters.
middle_index=len(string_access)//2
middle_three = string_access[middle_index - 1:middle_index + 2]
print("Middle 3 characters:", middle_three)

# ✅6. Access and print every second character from a string using slicing.
every_second_char = string_access[::2]
print("Every second character:", every_second_char)

# ✅7. Print all vowels in a given string using indexing and conditions.
vowels = 'aeiouAEIOU'
vowel_list = ''
for char in string_access:
    if char in vowels:
        vowel_list += char
print("Vowels in the string:", vowel_list)

# ✅8. Extract the domain from an email like "user@gmail.com" using slicing.
email = "user@gmail.com"
at_index = email.index('@')
domain = email[at_index + 1:]
print("Email domain:", domain)

# ✅9. Check whether the first and last characters of a string are the same.
if string_access[0] == string_access[-1]:
    print("First and last characters are the same.")
else:
    print("First and last characters are different.")

# ✅10. Print the reverse of a string using slicing.
reversed_string = string_access[::-1]
print("Reversed string:", reversed_string)

# 🟦 SECTION 2: Immutability and Modification (11–15)


# ❌11. Try to modify a single character in a string (to understand immutability).

sample = "hello"

    # sample[0] = "H"

# ✅12. Write code to change the first character of a string using slicing and concatenation.
original = "hello"
modified = "H" + original[1:]
print("Modified string:", modified)

# ✅13. Replace a character in the middle of a string by reconstructing it.
original = "python"
index = len(original) // 2 
modified = original[:index] + "X" + original[index + 1:]
print("Middle character replaced:", modified)


# ✅14. Create a function that replaces all vowels in a string with '*'.
 
def replace_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char in vowels:
            result += "*"
        else:
            result += char
    return result

print(replace_vowels("Education is Power"))



# ✅15. Create a function that returns a new string by replacing all occurrences of 'a' with '@'.
def replacewith(text):
    return text.replace('a', '@').replace('A', '@')

print(replacewith("Apples and bananas"))

# 🟦 SECTION 3: Deleting and Updating Strings (16–20)

# ✅16. Create a string and delete it using del, then try to print it (catch the error).
try:
    my_string = "This will be deleted"
    del my_string 
    print(my_string)  
except NameError as e:
    print("Error:", e)


# ✅17. Concatenate two strings using + and print the result.
text1 = "Reading"
text2 = "a book"
combined = text1 +" "+ text2
print("After Concatenation : ", combined)



# ✅18. Write a program that takes a name and appends "Welcome!" to it.
name = input("Enter your name: ")
message = name + ", Welcome!"
print(message)




# ✅19. Take user input and create a new sentence by combining it with a fixed phrase.
activity = input("What are you learning today? ")
sentence = "That's great! Keep practicing " + activity + "."
print(sentence)


# ✅20. Repeat the word "Hello" 5 times using the * operator.
repeat_message = "Hello " * 5
print(repeat_message.strip())

# 🟦 SECTION 4: Common String Methods (21–35)

# ✅21. Use len() to count the characters in a string.
new_string = "HelloWorld"
counting = len(new_string)
print(f"length of {new_string} is {counting}")

# ✅22. Convert a string to lowercase using .lower().

print("REETHA".lower())

# ✅23. Convert a string to uppercase using .upper().
print("reetha".upper())


# ✅24. Remove leading and trailing whitespaces using .strip().
text = "   nishareetha   "
print(text.strip())


# ✅25. Use .replace() to change "bad" to "good" in a sentence.
sentence = "Reading is a bad habit"
modify = sentence.replace("bad", "good")
print(f"modified sentence is: {modify}")


# ✅26. Split a comma-separated string into a list using .split(',').
colors = "red,green,blue"
item = colors.split(',')
print(item)


# ✅27. Join a list of words with - using .join().
words = ["join", "these", "words"]
joined = " ".join(words)
print("Joined string:", joined)  



# ✅28. Count how many times "a" appears in "banana" using .count().
print("banana".count("a"))


# ✅29. Use .find() to get the first index of the letter 'o' in "Google".
print("google".find('o'))



# ✅30. Create a program to convert 'Python is FUN' to 'python-is-fun'.
text = "Python is FUN"
converted = text.lower().replace(" ", "-")
print("Converted string:", converted)



# ✅31. Write a function that counts vowels and consonants in a string.
def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

v, c = count_vowels_consonants("Hello World!")
print("Vowels:", v, "Consonants:", c)


# ✅32. Use .replace() to remove all spaces from a string.
text = "Remove all spaces please"
no_spaces = text.replace(" ", "")
print(no_spaces)  


# ✅33. Use .split() and a for loop to print each word on a new line.

sentence = "Print each word in a new line"
for word in sentence.split():
    print(word)



# ✅34. Print the middle character of a string (if odd length).
text = "small"
if len(text) % 2 != 0:
    mid_index = len(text) // 2
    print("Middle character:", text[mid_index])
else:
    print("String has even length.")



# ✅35. Write a function that returns the first and last characters combined.

def first_and_last(text):
    if len(text) >= 2:
        return text[0] + text[-1]
    elif len(text) == 1:
        return text * 2
    else:
        return ""

print(first_and_last("Python"))  


# 🟦 SECTION 5: Concatenation and Repetition (36–40)

# ✅36. Concatenate first name and last name with a space in between.
first_name = "Nisha"
last_name = "Reetha"
full_name = first_name +" "+ last_name
print(f"Full name is : {full_name}")


# ✅37. Write a program that asks for a name and prints it 3 times using *.
get_name = input("Enter Your name: ")
repeat = get_name * 3
print(repeat)

# ✅38. Create a sentence by joining five different words using +.

sentence = "Python" + " " + "is" + " " + "fun" + " " + "to" + " " + "learn."
print(sentence)


# ✅39. Use .join() to combine a list of characters into a word.

list_items = ["s","t","r","i","n","g"]
join_items = "" .join(list_items)
print(join_items)


# ✅40. Take user input for a name and print “Welcome <name>” using string concatenation. 
get_input = input("Enter your name: ")
greet = "Welcome "+ get_input
print(greet)

# 🟦 SECTION 6: String Formatting (41–50)
                                 
# ✅41. Use f-string to print “My name is John and I am 30 years old.”
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old")


# ✅42. Use .format() to insert 2 numbers and print their sum.

a = 10
b = 20
print("The sum of {} and {} is {}".format(a, b, a + b))


# ✅43. Use % formatting to display the price of a product: "%s costs ₹%.2f"
product = "Phone"
price = 25999.99
print("%s costs ₹%.2f" % (product, price))


# ✅44. Create a function that takes name and marks and prints a result using all 3 formatting methods.

def print_result(name, marks):
    # f-string
    print(f"F-String: {name} scored {marks} marks.")
    # .format()
    print("Format: {} scored {} marks.".format(name, marks))
    # % formatting
    print("Percent: %s scored %d marks." % (name, marks))

print_result("Reetha", 92)



# ✅45. Format a list of products and their prices into a formatted table using f-strings.
products = [("Pen", 10), ("Notebook", 45), ("Bag", 799)]

print(f"{'Product':<10} {'Price (₹)':>10}")
print("-" * 22)
for item, cost in products:
    print(f"{item:<10} ₹{cost:>9.2f}")



# ✅46. Ask for user input (name, age) and print using .format().

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello {}, you are {} years old.".format(name, age))


# ✅47. Print temperature conversion: "Temperature is 35°C or 95°F" using f-string.
celsius = 35
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature is {celsius}°C or {fahrenheit}°F")



# ✅48. Format a sentence where the price changes dynamically: "The discounted price is ₹999"
price = 999
print(f"The discounted price is ₹{price}")



# ✅49. Write a function that accepts employee details and formats them using f-string.

def format_employee(emp_id, name, role, salary):
    return f"Employee {emp_id}: {name}, {role}, Salary: ₹{salary:.2f}"

print(format_employee(101, "Reetha", "Developer", 60000))


# ✅50. Create a dynamic weather report sentence using all formatting styles.
def weather_report(city, temp_c, condition):
    temp_f = (temp_c * 9/5) + 32
    # f-string
    print(f"{city} Weather Update:")
    # .format()
    print("Temperature: {}°C or {:.1f}°F".format(temp_c, temp_f))
    # % formatting
    print("Condition: %s" % condition)

weather_report("Doha", 42, "Sunny")
