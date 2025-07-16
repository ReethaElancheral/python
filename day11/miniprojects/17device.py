# 17. Device Connection Monitor

# Goal: Track connected devices to a server.
# Requirements:
# - Use set() to track current connections.
# - Use pop() when a device disconnects.
# - Use union() to merge multiple server logs.
# Concepts Covered: pop(), union(), membership.

# Initialize sets for active connections and server logs
active_devices = set()
server_logs = [
    {"device_01", "device_02", "device_03"},
    {"device_04", "device_02", "device_05"},
    {"device_01", "device_06", "device_07"}
]

# Function to simulate device disconnection
def disconnect_device(device_id):
    if device_id in active_devices:
        active_devices.remove(device_id)
        print(f"Device {device_id} disconnected.")
    else:
        print(f"Device {device_id} not found in active connections.")

# Function to simulate device reconnection
def reconnect_device(device_id):
    active_devices.add(device_id)
    print(f"Device {device_id} reconnected.")

# Function to merge server logs into active connections
def update_connections():
    global active_devices
    for log in server_logs:
        active_devices = active_devices.union(log)
    print("Active devices updated.")

# Simulate operations
update_connections()
disconnect_device("device_02")
reconnect_device("device_08")
print("Current active devices:", active_devices)
