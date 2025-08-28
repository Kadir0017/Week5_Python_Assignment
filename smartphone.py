# Parent Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in mAh

    # Method to display phone info
    def phone_info(self):
        return f"{self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}mAh"

    # Method to simulate making a call
    def make_call(self, number):
        return f"📞 Calling {number} from {self.model}..."

    # Method to simulate battery usage
    def use_battery(self, hours):
        used = hours * 200  # assume 200mAh per hour
        self.battery -= used
        return f"🔋 Battery remaining: {self.battery}mAh"


# Child Class (Inheritance)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu):
        # Call parent constructor
        super().__init__(brand, model, storage, battery)
        self.gpu = gpu

    # Polymorphism: overriding method
    def phone_info(self):
        return f"{self.brand} {self.model} (Gaming Edition) | {self.storage}GB | {self.battery}mAh | GPU: {self.gpu}"

    # Extra method for gaming
    def play_game(self, game, hours):
        self.use_battery(hours * 2)  # gaming drains battery faster
        return f"🎮 Playing {game} for {hours} hours on {self.model}!"


# -------------------
# Test the Classes
# -------------------

# Create normal smartphone
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 5000)
print(phone1.phone_info())
print(phone1.make_call("+254712345678"))
print(phone1.use_battery(3))

print("")

# Create gaming smartphone
gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 512, 6000, "Adreno 730")
print(gaming_phone.phone_info())
print(gaming_phone.play_game("PUBG Mobile", 2))
print(gaming_phone.make_call("+254700123456"))
