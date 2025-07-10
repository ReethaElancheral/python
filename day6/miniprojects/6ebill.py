# 🧩 6. Electricity Bill Calculator

# Topics Covered: def, return, *args, conditional
# Requirements:
# Take monthly units as arguments
# Calculate and return the bill using slabs
# Add GST using lambda

def calculate_bill(*units_list):
    total_bill = 0

    for units in units_list:
        if units <= 100:
            bill = units * 1.5
        elif units <= 200:
            bill = (100 * 1.5) + ((units - 100) * 2.5)
        elif units <= 300:
            bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)
        else:
            bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + ((units - 300) * 6)

        total_bill += bill

    add_gst = lambda amount: amount + (amount * 0.18)
    final_bill = add_gst(total_bill)

    return round(final_bill, 2)

print("Total Bill (with GST): ₹", calculate_bill(120, 250, 310))
