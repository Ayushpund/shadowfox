class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Super Power: {self.super_power}, Weapon: {self.weapon}"

    def is_leader(self):
        leaders = ["Captain America", "Iron Man", "Black Widow", "Hulk", "Thor", "Hawkeye"]
        return self.name in leaders

# Superheroes and their details
super_heroes = [
    {"name": "Captain America", "age": 100, "gender": "Male", "super_power": "Super strength", "weapon": "Shield"},
    {"name": "Iron Man", "age": 45, "gender": "Male", "super_power": "Technology", "weapon": "Armor"},
    {"name": "Black Widow", "age": 35, "gender": "Female", "super_power": "Superhuman", "weapon": "Batons"},
    {"name": "Hulk", "age": 40, "gender": "Male", "super_power": "Unlimited Strength", "weapon": "No Weapon"},
    {"name": "Thor", "age": 1500, "gender": "Male", "super_power": "Super Energy", "weapon": "Mjölnir"},
    {"name": "Hawkeye", "age": 45, "gender": "Male", "super_power": "Fighting skills", "weapon": "Bow and Arrows"}
]

# Create Avengers
avengers = []
for hero in super_heroes:
    avenger = Avenger(hero["name"], hero["age"], hero["gender"], hero["super_power"], hero["weapon"])
    avengers.append(avenger)

# Print information about each Avenger
for avenger in avengers:
    print(avenger.get_info())
    if avenger.is_leader():
        print(f"{avenger.name} is a leader.")
    else:
        print(f"{avenger.name} is not a leader.")
    print()
