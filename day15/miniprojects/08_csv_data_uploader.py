# 8. CSV Data 

# Use Case: Upload and validate CSV data. 
# Exception Handling Goals:
# Handle FileNotFoundError, ValueError, and parsing issues
# Raise InvalidCSVFormatError
# Use try-except-else-finally for parsing and cleanup
# Log invalid rows

import csv
import logging

# Setup logging
logging.basicConfig(filename="csv_upload_errors.log", level=logging.ERROR)

# Custom Exception
class InvalidCSVFormatError(Exception):
    pass

def upload_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if reader.fieldnames is None:
                raise InvalidCSVFormatError("CSV file is missing headers.")

            valid_rows = []
            row_num = 1
            for row in reader:
                try:
                   
                    if not row.get('name') or not row.get('age'):
                        raise InvalidCSVFormatError(f"Missing required fields in row {row_num}.")

                    age = int(row['age'])
                    if age < 0:
                        raise ValueError(f"Negative age in row {row_num}.")

                    valid_rows.append(row)

                except (InvalidCSVFormatError, ValueError) as e:
                    logging.error(f"Row {row_num} invalid: {e}")
                    print(f"❌ Row {row_num} invalid: {e}")
                row_num += 1

    except FileNotFoundError:
        print("❌ File not found.")
    except InvalidCSVFormatError as ice:
        print(f"❌ Invalid CSV format: {ice}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    else:
        print(f"✅ CSV uploaded successfully with {len(valid_rows)} valid rows.")
    finally:
        print("📝 CSV upload process complete.")


if __name__ == "__main__":
    path = input("Enter CSV file path: ")
    upload_csv(path)
