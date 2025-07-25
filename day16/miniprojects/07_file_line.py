# 7. File Line Reader 

# Goal: Read a text file using manual iterator approach. 
# Requirements: 
#  Use iter() on file object 
#  Use next() and StopIteration to end 
#  Print only non-empty lines 

print("Reading non-empty lines from file:")
with open("sample.txt") as f:
    it = iter(f)
    while True:
        try:
            line = next(it).strip()
            if line:
                print(line)
        except StopIteration:
            break
