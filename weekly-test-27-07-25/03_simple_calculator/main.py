from calculator.core import evaluate_expression
from calculator.memory import store, recall
from calculator.history import add_to_history, view_history
from calculator.converter import convert_length, convert_weight

def main():
    while True:
        print("\n=== Simple Calculator ===")
        print("1. Calculate expression")
        print("2. Store last result in memory")
        print("3. Recall memory")
        print("4. View calculation history")
        print("5. Convert units")
        print("0. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            expr = input("Enter expression: ")
            result = evaluate_expression(expr)
            print(f"Result: {result}")
            add_to_history(expr, result)
            last_result = result

        elif choice == "2":
            try:
                store(last_result)
                print("Stored last result in memory.")
            except NameError:
                print("No calculation done yet.")

        elif choice == "3":
            mem = recall()
            if mem is not None:
                print(f"Memory: {mem}")
            else:
                print("Memory is empty.")

        elif choice == "4":
            history = view_history()
            if not history:
                print("No history available.")
            else:
                for i, (expr, res) in enumerate(history, 1):
                    print(f"{i}. {expr} = {res}")

        elif choice == "5":
            print("a. Length conversion")
            print("b. Weight conversion")
            conv_choice = input("Choose conversion type: ").lower()
            if conv_choice == "a":
                value = float(input("Enter value: "))
                from_unit = input("From unit (m/cm/mm/km): ").lower()
                to_unit = input("To unit (m/cm/mm/km): ").lower()
                result = convert_length(value, from_unit, to_unit)
                print(f"Converted value: {result}")
            elif conv_choice == "b":
                value = float(input("Enter value: "))
                from_unit = input("From unit (kg/g/mg): ").lower()
                to_unit = input("To unit (kg/g/mg): ").lower()
                result = convert_weight(value, from_unit, to_unit)
                print(f"Converted value: {result}")
            else:
                print("Invalid conversion choice.")

        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
