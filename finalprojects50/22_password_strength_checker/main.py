# 22. Password Strength Checker 
# Objective: Rate password strength (Weak/Medium/Strong). 
# Requirements: 
#  String Operations: Check length, special chars. 
#  Conditionals: Score based on rules (e.g., +1 for uppercase). 
#  Dictionary: Strength thresholds ({"Weak": <6, ...}). 
#  Exception Handling: Empty input. 
#  Functions: evaluate_strength(). 
#  Loops: Re-prompt until strong password. 
#  Generator: Yield missing criteria (e.g., "Add a number").



from password_checker import evaluate_strength, password_criteria

def main():
    print("🔐 Welcome to Password Strength Checker")
    while True:
        try:
            pwd = input("Enter your password: ").strip()
            if not pwd:
                raise ValueError("Password cannot be empty!")

            strength, score = evaluate_strength(pwd)
            print(f"💡 Strength: {strength} ({score}/5)")

            if strength != "Strong":
                print("❗ Suggestions:")
                for tip in password_criteria(pwd):
                    print(f"  - {tip}")
            else:
                print("✅ Password is strong!")
                break

        except ValueError as ve:
            print(f"Error: {ve}")

if __name__ == "__main__":
    main()
