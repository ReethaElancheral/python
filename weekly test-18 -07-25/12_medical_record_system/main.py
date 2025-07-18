from healthcare.healthcare_records import add_record, view_records

def main():
    records = {}

    while True:
        print("\n1. Add Medical Record")
        print("2. View All Records")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            pid = input("Enter Patient ID: ").strip()
            name = input("Enter Name: ").strip()
            age = input("Enter Age: ").strip()
            illness_input = input("Enter illnesses (comma-separated): ").strip()
            illnesses = [ill.strip().title() for ill in illness_input.split(",") if ill.strip()]

            add_record(pid, name, age, illnesses, records)

        elif choice == "2":
            view_records(records)

        elif choice == "3":
            print("Exiting Medical Record System.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
