def check_restock_alerts(inventory, threshold=10):
    print("\n--- Restock Alerts ---")
    alerts = False
    for item, ((qty, _), _, _) in inventory.items():
        if qty < threshold:
            print(f"ALERT: {item} is low on stock! (Qty: {qty})")
            alerts = True
    if not alerts:
        print("All items are sufficiently stocked.")
