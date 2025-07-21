# 12. Smart Home Control System

# Concepts: Composition, Polymorphism, Method Overriding
# Classes:  Device, Light, AC, Fan, SmartHub
# Requirements:
# Turn on/off devices
# Use polymorphism for operate() method
# Compose SmartHub with devices

class Device:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def operate(self):
        raise NotImplementedError("Subclasses must implement operate method")

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} turned ON.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} turned OFF.")

class Light(Device):
    def operate(self):
        if self.is_on:
            print(f"{self.name} is glowing brightly.")
        else:
            print(f"{self.name} is off.")

class AC(Device):
    def operate(self):
        if self.is_on:
            print(f"{self.name} is cooling the room.")
        else:
            print(f"{self.name} is off.")

class Fan(Device):
    def operate(self):
        if self.is_on:
            print(f"{self.name} is spinning.")
        else:
            print(f"{self.name} is off.")

class SmartHub:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        print(f"{device.name} added to SmartHub.")

    def operate_all(self):
        print("Operating all devices:")
        for device in self.devices:
            device.operate()

    def turn_all_on(self):
        for device in self.devices:
            device.turn_on()

    def turn_all_off(self):
        for device in self.devices:
            device.turn_off()

def main():
    hub = SmartHub()

    light = Light("Living Room Light")
    ac = AC("Bedroom AC")
    fan = Fan("Ceiling Fan")

    hub.add_device(light)
    hub.add_device(ac)
    hub.add_device(fan)

    # Turn all devices ON and operate
    hub.turn_all_on()
    hub.operate_all()

    # Turn all devices OFF and operate
    hub.turn_all_off()
    hub.operate_all()

if __name__ == "__main__":
    main()
