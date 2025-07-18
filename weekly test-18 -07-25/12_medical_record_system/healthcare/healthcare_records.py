def add_record(patient_id, name, age, illnesses, records):
    pid = (patient_id,)  # Tuple to make it immutable

    if pid in records:
        print(f"Patient {patient_id} already exists.")
        return

    records[pid] = {
        "name": name,
        "age": age,
        "illnesses": set(illnesses)
    }
    print(f"Medical record added for {name}.")

def view_records(records):
    if not records:
        print("No records found.")
        return

    print("\n--- All Medical Records ---")
    for pid, data in records.items():
        print(f"ID: {pid[0]}, Name: {data['name']}, Age: {data['age']}")
        print(f"Diagnosed with: {', '.join(data['illnesses'])}")
        print("-" * 30)
