import os

INVOICE_DIR = "invoices"

def get_next_invoice_id():
    if not os.path.exists(INVOICE_DIR):
        os.makedirs(INVOICE_DIR)
        return 1
    existing_files = os.listdir(INVOICE_DIR)
    invoice_ids = [
        int(f.split("_")[1].split(".")[0])
        for f in existing_files if f.startswith("invoice_") and f.endswith(".txt")
    ]
    return max(invoice_ids, default=0) + 1

def create_invoice():
    customer_name = input("Customer Name: ").strip()
    customer_phone = input("Customer Phone: ").strip()
    order_details = []
    print("Enter order items (type 'done' to finish):")
    while True:
        item = input("Item name: ").strip()
        if item.lower() == "done":
            break
        quantity = input("Quantity: ").strip()
        price = input("Price per item (₹): ").strip()
        try:
            quantity = int(quantity)
            price = float(price)
        except ValueError:
            print("❌ Invalid quantity or price. Try again.")
            continue
        order_details.append((item, quantity, price))

    if not order_details:
        print("❌ No items added, invoice not created.")
        return

    invoice_id = get_next_invoice_id()
    filename = os.path.join(INVOICE_DIR, f"invoice_{invoice_id:03d}.txt")

    total_amount = sum(q * p for _, q, p in order_details)

    with open(filename, "w") as f:
        f.write(f"Invoice ID: {invoice_id:03d}\n")
        f.write(f"Customer Name: {customer_name}\n")
        f.write(f"Customer Phone: {customer_phone}\n")
        f.write("=" * 40 + "\n")
        f.write(f"{'Item':20} {'Qty':5} {'Price (₹)':10} {'Total (₹)':10}\n")
        f.write("-" * 40 + "\n")
        for item, qty, price in order_details:
            f.write(f"{item:20} {qty:<5} ₹{price:<10.2f} ₹{qty * price:<10.2f}\n")
        f.write("-" * 40 + "\n")
        f.write(f"Total Amount: ₹{total_amount:.2f}\n")
        f.write("=" * 40 + "\n")

    print(f"✅ Invoice generated and saved as {filename}")
