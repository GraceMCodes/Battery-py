class Smartphone:
    def __init__(self, model, os, battery_life, storage_capacity):
        # Constructor to initialize the attributes
        self.model = model
        self.os = os
        self.battery_life = battery_life  # in hours
        self.storage_capacity = storage_capacity  # in GB

    def make_call(self, number):
        print(f"Dialing {number} from {self.model}... 📞")

    def send_text(self, number, message):
        print(f"Sending message to {number}: {message} ✉️")

    def check_battery(self):
        print(f"Battery life remaining: {self.battery_life} hours 🔋")

    def install_app(self, app_name, app_size):
        if app_size <= self.storage_capacity:
            self.storage_capacity -= app_size
            print(f"{app_name} installed! Remaining storage: {self.storage_capacity}GB 📱")
        else:
            print(f"Not enough storage to install {app_name} ❌")


# Example usage:
phone1 = Smartphone("iPhone 15", "iOS", 20, 128)
phone1.make_call("123-456-7890")
phone1.send_text("123-456-7890", "Hey, how's it going?")
phone1.check_battery()
phone1.install_app("Instagram", 2)

