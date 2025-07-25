# 3. Custom CSV Row Reader 
# Objective: Create a file reader generator to fetch each row from a .csv file. 
# Requirements: 

#  Use open() and yield per line. 
#  Clean each row lazily. 
#  Skip header using next(). 
#  Stop if "END" keyword is detected in any row.

def csv_row_reader(filepath):
    with open(filepath, "r") as file:
        next(file)  # skip header
        for row in file:
            if "END" in row:
                break
            yield row.strip()



print("Reading CSV rows (until 'END'):")
for line in csv_row_reader("sample.csv"):
    print(line)
