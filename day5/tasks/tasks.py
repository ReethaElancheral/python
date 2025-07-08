# ✅ 🔁 Basic While Loop Tasks (1–10)

# Task 1: Print numbers from 1 to 10 using a while loop.
num = 1
while (num<=10):
    print(num)
    num+=1

# Task 2: Print even numbers from 2 to 20 using a while loop.
num_1 = 1
while num_1 <= 20:
    if num_1 % 2 != 0:
        num_1 += 1
        continue
    print(num_1)
    num_1 += 1

   
# Task 3: Print the reverse numbers from 10 to 1.
i_num = 10
while i_num >= 1:
    print(i_num)
    i_num -= 1


# Task 4: Ask the user to enter a number and print all numbers up to that number.
n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(i)
    i += 1


# Task 5: Calculate the sum of numbers from 1 to 50 using while.
i = 1
total = 0
while i <= 50:
    total += i
    i += 1
print("Total sum:", total)


# Task 6: Find the factorial of a number using a while loop.
n = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print("Factorial:", factorial)


# Task 7: Print all multiples of 3 between 1 and 30.
i = 1
while i <= 30:
    if i % 3 == 0:
        print(i)
    i += 1


# Task 8: Take user input until they type "stop".
while True:
    user_input = input("Enter something (type 'stop' to end): ")
    if user_input.lower() == "stop":
        break
    print("You entered:", user_input)


# Task 9: Count from 100 down to 50 in steps of 5.
i = 100
while i >= 50:
    print(i)
    i -= 5


# Task 10: Take 5 inputs from user and store them in a list using a while loop.
user_inputs = []
count = 0
while count < 5:
    item = input(f"Enter item {count + 1}: ")
    user_inputs.append(item)
    count += 1

print("Your list:", user_inputs)


# ✅ ♾️ Infinite While Loop Tasks (11–15)

# Task 11: Create a while True loop that prints "Welcome!" infinitely (Manually stop it).
# while True:
#     print("Welcome!")


# Task 12: Create a login simulation that keeps asking for a correct password until it's matched.

correct_password = "python123"
while True:
    entered = input("Enter password: ")
    if entered == correct_password:
        print("✅ Access Granted!")
        break
    else:
        print("❌ Incorrect. Try again.")


# Task 13: Simulate a menu-based app using an infinite loop (while True) with exit option.
while True:
    print("\n📋 Menu:")
    print("1. Greet")
    print("2. Info")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print("👋 Hello, User!")
    elif choice == "2":
        print("ℹ️ This is a simple menu app.")
    elif choice == "3":
        print("👋 Exiting app. Bye!")
        break
    else:
        print("❌ Invalid choice.")


# Task 14: Continuously ask for a number until the user enters a negative number.
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        print("⛔ Negative number entered. Stopping.")
        break
    else:
        print(f"You entered: {num}")


# Task 15: Simulate an ATM system using an infinite loop with options: check balance, deposit, withdraw, exit.

balance = 1000

while True:
    print("\n🏧 ATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    option = input("Select an option: ")

    if option == "1":
        print(f"💰 Balance: ₹{balance}")
    elif option == "2":
        amount = float(input("Enter deposit amount: ₹"))
        balance += amount
        print(f"✅ Deposited ₹{amount}")
    elif option == "3":
        amount = float(input("Enter withdrawal amount: ₹"))
        if amount <= balance:
            balance -= amount
            print(f"✅ Withdrawn ₹{amount}")
        else:
            print("❌ Insufficient balance!")
    elif option == "4":
        print("👋 Thank you! Exiting ATM.")
        break
    else:
        print("❌ Invalid option. Try again.")

# ✅ 🔂 While with continue Statement (16–25)

# Task 16: Print odd numbers from 1 to 20 using continue.
num = 1
while num <= 20:
    if num % 2 == 0:
        num += 1
        continue
    print(num)
    num += 1



# Task 17: Ask the user to enter 5 numbers. Skip the number if it is negative using continue.
count = 0
while count < 5:
    number = int(input("Enter a number: "))
    if number < 0:
        print("Skipped negative number.")
        continue
    print("You entered:", number)
    count += 1


# Task 18: Print numbers from 1 to 10, but skip 5 using continue.
num = 1
while num <= 10:
    if num == 5:
        num += 1
        continue
    print(num)
    num += 1


# Task 19: Print all numbers from 1 to 20 except those divisible by 3.
num = 1
while num <= 20:
    if num % 3 == 0:
        num += 1
        continue
    print(num)
    num += 1


# Task 20: Ask the user to enter 10 words. Skip if the word is less than 3 characters.
count = 0
while count < 10:
    word = input("Enter a word: ")
    
    if len(word) < 3:
        print("Skipped short word.")
        continue

    print("Accepted word:", word)
    count += 1 





# Task 21: Print only vowels from the string "python programming" using while and continue.
text = "python programming"
i = 0
while i < len(text):
    if text[i].lower() not in "aeiou":
        i += 1
        continue
    print(text[i])
    i += 1


# Task 22: Count how many odd numbers exist between 1 and 100.
num = 1
count = 0
while num <= 100:
    if num % 2 == 0:
        num += 1
        continue
    count += 1
    num += 1
print("Odd numbers between 1 and 100:", count)


# Task 23: Keep asking user for numbers and print only if it's a multiple of 5.
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    if number % 5 != 0:
        continue
    print("Multiple of 5:", number)


# Task 24: Skip printing numbers divisible by both 2 and 3 from 1 to 30.
num = 1
while num <= 30:
    if num % 2 == 0 and num % 3 == 0:
        num += 1
        continue
    print(num)
    num += 1


# Task 25: Skip even numbers and print the cube of odd numbers between 1 and 20.

num = 1
while num <= 20:
    if num % 2 == 0:
        num += 1
        continue
    print(f"{num}³ = {num**3}")
    num += 1


# ✅ 🛑 While with break Statement (26–35)

# Task 26: Print numbers from 1 to 10 and break the loop if number is 6.
num = 1
while num <= 10:
    if num == 6:
        break
    print(num)
    num += 1



# Task 27: Ask the user to enter numbers. Break the loop when user enters 0.
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        print("⛔ Loop stopped.")
        break
    print("You entered:", num)


# Task 28: Create a simple password checker. Break the loop if the correct password is entered.
correct_password = "python123"
while True:
    entered = input("Enter password: ")
    if entered == correct_password:
        print("✅ Access granted!")
        break
    else:
        print("❌ Wrong password. Try again.")



# Task 29: Print numbers from 1 to 100. Break the loop when a number divisible by 17 is found.
num = 1
while num <= 100:
    if num % 17 == 0:
        print(f"🔴 Found divisible by 17: {num}")
        break
    print(num)
    num += 1



# Task 30: Keep asking for user input until they type "exit" (use break to stop).
while True:
    text = input("Type something (type 'exit' to stop): ")
    if text.lower() == "exit":
        print("👋 Exiting...")
        break
    print("You typed:", text)


# Task 31: Simulate a game loop: “Press q to quit”.
while True:
    command = input("Press 'q' to quit the game: ")
    if command.lower() == "q":
        print("🎮 Game Over")
        break
    print("✅ Game continues...")



# Task 32: Ask the user 10 questions, stop early if any answer is empty using break.
count = 1
while count <= 10:
    answer = input(f"Question {count}: ")
    if answer == "":
        print("❌ Empty answer. Exiting.")
        break
    count += 1


# Task 33: Simulate 3 login attempts. Break the loop if login is successful.
correct_username = "admin"
correct_password = "pass123"
attempts = 0

while attempts < 3:
    username = input("Username: ")
    password = input("Password: ")
    if username == correct_username and password == correct_password:
        print("✅ Login Successful!")
        break
    else:
        print("❌ Invalid credentials.")
    attempts += 1

if attempts == 3:
    print("🚫 Account Locked.")


# Task 34: Print the multiplication table of 5, but stop if the product exceeds 30.
i = 1
while True:
    product = 5 * i
    if product > 30:
        break
    print(f"5 x {i} = {product}")
    i += 1


# Task 35: Count from 1 to 10. If number is 7, break the loop and print “Loop Interrupted”.

num = 1
while num <= 10:
    if num == 7:
        print("⚠️ Loop Interrupted at 7")
        break
    print(num)
    num += 1

# ✅ 📝 While with pass Statement (36–40)

# Task 36: Loop through 1 to 5 and use pass when number is 3.
i = 1
while i <= 5:
    if i == 3:
        pass  
    print(i)
    i += 1


# Task 37: Simulate a placeholder loop for future features.
i = 1
while i <= 3:
    pass  
    i += 1
print("Loop simulated with placeholder pass")


# Task 38: Create a loop where you skip logic for even numbers using pass.
i = 1
while i <= 5:
    if i % 2 == 0:
        i += 1
        pass  
        continue
    print(i)
    i += 1


# Task 39: Use a loop that prints numbers 1 to 5 and uses pass when number is 2 or 4.
i = 1
while i <= 5:
    if i == 2 or i == 4:
        pass  
    print(i)
    i += 1


# Task 40: Create a loop that runs without errors using pass as a placeholder for missing logic.
i = 1
while i <= 3:
    pass 
    i += 1
print("Loop executed with pass only")


# ✅ 🔚 While with else Statement (41–45)

# Task 41: Print numbers from 1 to 3. Use else to print "Loop Finished".
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop Finished")


# Task 42: Ask the user to enter 3 numbers. Use else to say “All numbers entered successfully”.
count = 0
while count < 3:
    num = input("Enter a number: ")
    if num == "":
        print("Empty input!")
        break
    count += 1
else:
    print("All numbers entered successfully")


# Task 43: Run a loop to print even numbers till 10. Use break to exit early. Ensure else doesn’t run.
num = 2
while num <= 10:
    if num == 6:
        print("Breaking early at", num)
        break
    if num % 2 == 0:
        print(num)
    num += 1
else:
    print("This will not run because loop was broken.")


# Task 44: Print numbers from 1 to 5. If loop finishes without break, print “Nice job!”.
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Nice job!")


# Task 45: Create a password checker with 3 attempts. If successful, print inside else.
correct_password = "pass123"
attempts = 0

while attempts < 3:
    user_input = input("Enter password: ")
    if user_input == correct_password:
        print("Access granted.")
        break
    else:
        print("Wrong password.")
    attempts += 1
else:
    print("3 wrong attempts. Access denied.")


# ✅ 🔁 Logical/Practical Looping Use-Cases (46–50)

# Task 46: Ask the user to input 5 student names using while and store them in a list.
students = []
count = 0

while count < 5:
    name = input(f"Enter student name {count + 1}: ")
    students.append(name)
    count += 1

print("Student List:", students)


# Task 47: Create a menu-driven loop for a to-do list app (add, view, remove, exit).
todo_list = []

while True:
    print("\nTo-Do Menu:\n1. Add\n2. View\n3. Remove\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task to add: ")
        todo_list.append(task)
        print("Task added.")
    elif choice == "2":
        print("To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    elif choice == "3":
        task = input("Enter task to remove: ")
        if task in todo_list:
            todo_list.remove(task)
            print("Task removed.")
        else:
            print("Task not found.")
    elif choice == "4":
        print("Exiting To-Do App.")
        break
    else:
        print("Invalid choice.")


# Task 48: Ask the user to enter age of 5 people. Print how many are adults (age ≥ 18).
count = 0
adults = 0

while count < 5:
    age = int(input(f"Enter age of person {count + 1}: "))
    if age >= 18:
        adults += 1
    count += 1

print(f"Number of adults (18+): {adults}")


# Task 49: Create a quiz loop: keep asking until the user gets the correct answer.
answer = "paris"

while True:
    user_answer = input("What is the capital of France? ").lower()
    if user_answer == answer:
        print("Correct!")
        break
    else:
        print("Try again.")


# Task 50: Build a basic number guessing game. User keeps guessing until the correct number is entered.
import random
secret = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret:
        print("🎉 Correct! You guessed it.")
        break
    else:
        print("❌ Wrong. Try again.")
