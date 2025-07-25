# 13. Unique ID Generator 
# Objective: Generate unique transaction or session IDs on demand. 
# Requirements: 
#  Infinite generator with format: TRX001, TRX002, ... 
#  Can reset from a custom point using send(). 
#  Use StopIteration for demo purposes after 1000 IDs. 

def unique_id_generator():
    count = 1
    while count <= 1000:
        new_start = yield f"TRX{count:03}"
        if new_start:
            count = int(new_start)
        else:
            count += 1
    return "1000 IDs generated"

# Example usage:
ids = unique_id_generator()
print(next(ids))  # TRX001
print(next(ids))  # TRX002
print(ids.send("200"))  # TRX200

try:
    for _ in range(800):
        print(next(ids))
except StopIteration as e:
    print(e.value)
