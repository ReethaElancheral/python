# 8. Order Processing Queue 
# Objective: Simulate an online order processor that handles orders lazily. 
# Requirements: 
#  Use yield to emit next order. 
#  Pause and resume using send(). 
#  Use return when orders are completed and print a summary. 

def order_processor(orders):
    total = 0
    paused = False
    try:
        for order in orders:
            control = yield order
            if control == "pause":
                paused = True
                while paused:
                    control = yield "Paused..."
                    if control == "resume":
                        paused = False
            total += 1
    finally:
        return f"All {total} orders processed!"

# Example usage:
orders = ["Order#101", "Order#102", "Order#103"]
processor = order_processor(orders)

print("Order Processing:")
print(next(processor))  # Order#101
print(processor.send("pause"))
print(processor.send("still paused"))
print(processor.send("resume"))  # Order#102
print(next(processor))  # Order#103

try:
    print(next(processor))  # Should raise StopIteration
except StopIteration as e:
    print(e.value)  # Final summary
