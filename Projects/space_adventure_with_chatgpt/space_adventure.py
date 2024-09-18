import os
import random
import math
from openai import OpenAI

# Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-4o-mini"

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

class Player:
    def __init__(self, name):
        self.name = name
        self.experience = 0
        self.skills = {}

    def gain_experience(self, amount):
        self.experience += amount

    def learn_skill(self, skill_name):
        self.skills[skill_name] = self.skills.get(skill_name, 0) + 1

class ShipType:
    def __init__(self, name, hull, shields, engines, sensors, weapons, cargo, fuel, description):
        self.name = name
        self.hull = hull
        self.shields = shields
        self.engines = engines
        self.sensors = sensors
        self.weapons = weapons
        self.cargo = cargo
        self.fuel = fuel
        self.description = description

SHIP_TYPES = {
    "Hauler": ShipType("Hauler", "Heavy", "Medium", "Slow", "Basic", "Unarmed", 500, 200,
                       "A large, slow vessel designed for transporting cargo across vast distances."),
    "Mining Vessel": ShipType("Mining Vessel", "Medium", "Medium", "Slow", "Advanced", "Light", 400, 150,
                              "Equipped with advanced sensors and specialized equipment for resource extraction."),
    "Scout Vessel": ShipType("Scout Vessel", "Light", "Light", "Fast", "Advanced", "Light", 50, 120,
                             "Fast and stealthy, perfect for reconnaissance and exploration."),
    "Bomber": ShipType("Bomber", "Medium", "Light", "Medium", "Basic", "Heavy", 100, 100,
                       "Heavily armed with powerful long-range weapons, but vulnerable in close combat."),
    "Corvette": ShipType("Corvette", "Medium", "Medium", "Fast", "Medium", "Medium", 80, 110,
                         "A versatile, well-rounded small warship suitable for various missions."),
    "Frigate": ShipType("Frigate", "Heavy", "Heavy", "Medium", "Medium", "Heavy", 150, 140,
                        "A medium-sized warship balancing firepower, defense, and utility."),
    "Destroyer": ShipType("Destroyer", "Heavy", "Heavy", "Medium", "Advanced", "Heavy", 100, 130,
                          "A powerful warship designed to escort larger vessels and engage enemy ships."),
    "Science Vessel": ShipType("Science Vessel", "Medium", "Medium", "Medium", "Advanced", "Light", 200, 140,
                               "Equipped with cutting-edge laboratories and sensors for research and analysis."),
    "Stealth Ship": ShipType("Stealth Ship", "Light", "Light", "Fast", "Advanced", "Medium", 40, 100,
                             "Designed for covert operations with advanced cloaking technology."),
    "Carrier": ShipType("Carrier", "Heavy", "Heavy", "Slow", "Advanced", "Fighter Wings", 300, 180,
                        "A massive ship capable of deploying smaller vessels and serving as a mobile base.")
}

class ShipStatus:
    def __init__(self, name, ship_type):
        self.name = name
        self.type = ship_type
        self.hull = 100
        self.systems = {
            "shields": 100,
            "engines": 100,
            "sensors": 100,
            "weapons": 100
        }
        self.cargo = 0
        self.max_cargo = ship_type.cargo
        self.fuel = ship_type.fuel
        self.max_fuel = ship_type.fuel

    def damage_system(self, system, amount):
        if system == "hull":
            self.hull = max(0, self.hull - amount)
        elif system in self.systems:
            self.systems[system] = max(0, self.systems[system] - amount)

    def repair_system(self, system, amount):
        if system == "hull":
            self.hull = min(100, self.hull + amount)
        elif system in self.systems:
            self.systems[system] = min(100, self.systems[system] + amount)

    def use_fuel(self, amount):
        self.fuel = max(0, self.fuel - amount)

    def refuel(self, amount):
        self.fuel = min(self.max_fuel, self.fuel + amount)

    def load_cargo(self, amount):
        space_left = self.max_cargo - self.cargo
        loaded = min(space_left, amount)
        self.cargo += loaded
        return loaded

    def unload_cargo(self, amount):
        unloaded = min(self.cargo, amount)
        self.cargo -= unloaded
        return unloaded

    def get_status_report(self):
        systems_report = ", ".join([f"{k}: {v}%" for k, v in self.systems.items()])
        return f"""Ship: {self.name} ({self.type.name})
Hull: {self.hull}% ({self.type.hull})
Fuel: {self.fuel}/{self.max_fuel}
Cargo: {self.cargo}/{self.max_cargo}
Systems: {systems_report}
Capabilities:
  Shields: {self.type.shields}
  Engines: {self.type.engines}
  Sensors: {self.type.sensors}
  Weapons: {self.type.weapons}"""

class Galaxy:
    def __init__(self, name, controlled_by):
        self.name = name
        self.controlled_by = controlled_by
        self.systems = []

class Universe:
    def __init__(self, start_location):
        self.galaxies = [
            Galaxy("Milky Way", "Human"),
            Galaxy("Andromeda", "Human"),
            Galaxy("Triangulum", "Human"),
            Galaxy("Centaurus A", "Bug"),
            Galaxy("Bode's Galaxy", "Bug"),
            Galaxy("Sculptor Galaxy", "Bug")
        ]
        self.current_galaxy = self.galaxies[0]
        self.current_location = start_location
        self.discovered_locations = [start_location]
        self.nearby_ships = []

    def travel_to(self, location, galaxy=None):
        self.current_location = location
        if galaxy:
            self.current_galaxy = galaxy
        if location not in self.discovered_locations:
            self.discovered_locations.append(location)
        self.update_nearby_ships()

    def get_current_location(self):
        return f"{self.current_location}, {self.current_galaxy.name}"

    def update_nearby_ships(self):
        self.nearby_ships = [ShipStatus(f"Unknown Ship {i}") for i in range(random.randint(0, 3))]
        if self.current_galaxy.controlled_by == "Bug" or random.random() < 0.1:
            self.nearby_ships.append(ShipStatus("Bug Warship"))

    def get_nearby_ships_report(self):
        if not self.nearby_ships:
            return "No other ships detected in the vicinity."
        return "Nearby ships: " + ", ".join([ship.name for ship in self.nearby_ships])

    def is_in_bug_territory(self):
        return self.current_galaxy.controlled_by == "Bug"

class EventSystem:
    def __init__(self):
        self.event_types = [
            "space_debris",
            "alien_encounter",
            "cosmic_phenomenon",
            "bug_interaction",
            "technological_discovery",
            "crew_incident"
        ]
        self.base_probability = 0.2
        self.current_probability = self.base_probability
        self.cooldown_factor = 0.1
        self.turns_since_last_event = 0

    def check_for_events(self, player, ship, universe):
        if random.random() < self.current_probability:
            event_type = random.choice(self.event_types)
            self.turns_since_last_event = 0
            self.current_probability = self.base_probability * 0.1
            return self.generate_event(event_type, player, ship, universe)
        else:
            self.turns_since_last_event += 1
            self.update_probability()
            return None

    def update_probability(self):
        recovery = 1 - math.exp(-self.cooldown_factor * self.turns_since_last_event)
        self.current_probability = self.base_probability - (self.base_probability - self.current_probability) * (1 - recovery)

    def generate_event(self, event_type, player, ship, universe):
        prompt = f"""Generate a brief, engaging space adventure event of type '{event_type}'. 
        The event should be unexpected and have a clear impact on the ship, crew, or mission. 
        Current location: {universe.get_current_location()}
        Nearby ships: {universe.get_nearby_ships_report()}
        Ship status: {ship.get_status_report()}
        
        Format the response as:
        Event: [Brief title of the event]
        Description: [2-3 sentences describing what happens]
        Impact: [1 sentence on how this affects the ship, crew, or mission]
        """

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=150
        )

        event_description = response.choices[0].message.content
        self.apply_event_impact(event_description, player, ship, universe)
        return event_description

    def apply_event_impact(self, event_description, player, ship, universe):
        if "shields" in event_description.lower():
            ship.damage_system("shields", random.randint(5, 20))
        if "engines" in event_description.lower():
            ship.damage_system("engines", random.randint(5, 20))
        if "experience" in event_description.lower():
            player.gain_experience(random.randint(5, 15))
        if "unknown location" in event_description.lower():
            universe.travel_to("Unknown Location")

class ChatInterface:
    def __init__(self, player_name, ship_name, start_location):
        self.messages = [
            {"role": "system", "content": f"""You are an advanced AI assistant for a lone space pilot named {player_name} on their ship '{ship_name}'. 
            The pilot is currently in {start_location}. Guide the pilot through their adventure, describe cosmic phenomena, and respond to their actions and queries. 
            When events occur or ship status changes, incorporate them into your responses. 
            Be aware that humanity is in an ongoing conflict with an alien species known as 'The Bugs'. 
            This conflict has a long and bloody history, with atrocities committed on both sides. 
            The Bugs can communicate with humans via translators, but interactions are tense and often hostile. 
            The known universe consists of 6 galaxies: Milky Way, Andromeda, and Triangulum (controlled by humans), 
            and Centaurus A, Bode's Galaxy, and Sculptor Galaxy (controlled by Bugs).
            Travel between galaxies is possible but requires significant fuel and can be dangerous."""}
        ]

    def get_initial_message(self):
        return "Greetings, pilot! Your ship's systems are online and awaiting your command. What would you like to do first in this unfamiliar territory?"

    def send_message(self, user_input, ship_status, nearby_ships, event_info=None):
        context = f"Current ship status: {ship_status}\n{nearby_ships}\n"
        if event_info:
            context += f"Event occurred: {event_info}\n"
        
        self.messages.append({"role": "system", "content": context})
        self.messages.append({"role": "user", "content": user_input})
        
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=self.messages
        )
        response = completion.choices[0].message.content
        self.messages.append({"role": "assistant", "content": response})
        return response

def print_instructions():
    print("""
Welcome to the AI Space Adventure!

Basic instructions:
1. Type your actions or dialogue as if you're interacting with your ship's AI.
2. Be descriptive in your actions to get more detailed responses.
3. Type 'help' at any time to see these instructions again.
4. Type 'quit' to end the mission.
5. Have fun and explore the vastness of space!

Remember, as a space pilot, you can attempt various actions. Some common ones include:
- Scan [area/object]
- Navigate to [coordinates/celestial body]
- Analyze [anomaly/signal]
- Use [ship system/equipment]
- Communicate with [alien life/other ships]

Your space adventure begins now. Good luck, pilot!
""")

def choose_starting_scenario():
    scenarios = [
        ("Sol System", "Stellar Voyager", "Earth's orbital space station", SHIP_TYPES["Corvette"]),
        ("Alpha Centauri", "Proxima Explorer", "the first extrasolar human colony", SHIP_TYPES["Scout Vessel"]),
        ("Sirius System", "Dogstar Patroller", "a military outpost guarding against Bug incursions", SHIP_TYPES["Destroyer"]),
        ("Betelgeuse Station", "Red Giant Observer", "a scientific research station studying the dying star", SHIP_TYPES["Science Vessel"]),
        ("Orion Nebula", "Stellar Nursery", "a mobile research platform studying star formation", SHIP_TYPES["Mining Vessel"]),
        ("Neutral Zone", "Diplomacy", "a space station in the neutral zone between human and Bug territories", SHIP_TYPES["Frigate"]),
        ("Custom", "Custom", "Create your own starting scenario", None)
    ]
    
    print("Choose your starting scenario:")
    for i, (location, ship, description, _) in enumerate(scenarios, 1):
        print(f"{i}. {location} - Aboard the {ship}, stationed at {description}.")
    
    while True:
        try:
            choice = int(input("Enter the number of your chosen scenario: "))
            if 1 <= choice <= len(scenarios):
                if choice == len(scenarios):
                    return create_custom_scenario()
                return scenarios[choice - 1]
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Please enter a valid number.")

def create_custom_scenario():
    print("\nCreating a custom starting scenario:")
    
    systems = ["Sol System", "Alpha Centauri", "Sirius System", "Betelgeuse", "Orion Nebula", "Neutral Zone"]
    print("\nAvailable star systems:")
    for i, system in enumerate(systems, 1):
        print(f"{i}. {system}")
    while True:
        try:
            system_choice = int(input("Choose your starting star system (enter the number): "))
            if 1 <= system_choice <= len(systems):
                start_system = systems[system_choice - 1]
                break
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Please enter a valid number.")

    job_title = input("\nEnter your job title or role (e.g., 'Space Trader', 'Xenobiologist', 'Bounty Hunter'): ")

    print("\nChoose your specific location:")
    print("1. Planet surface")
    print("2. Orbiting space station")
    print("3. Deep space")
    print("4. Custom location")
    while True:
        try:
            location_choice = int(input("Enter the number of your choice: "))
            if location_choice == 1:
                location = input("Enter the name of the planet: ")
            elif location_choice == 2:
                location = f"Space Station orbiting {input('Enter the name of the celestial body the station is orbiting: ')}"
            elif location_choice == 3:
                location = "Deep space"
            elif location_choice == 4:
                location = input("Describe your custom location: ")
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    ship_name = input("\nName your ship: ")

    ship_type = choose_ship_type()

    return (start_system, ship_name, f"{job_title} at {location}", ship_type)

def choose_ship_type():
    print("\nChoose your ship type:")
    for i, (name, ship_type) in enumerate(SHIP_TYPES.items(), 1):
        print(f"{i}. {name}: {ship_type.description}")
    
    while True:
        try:
            choice = int(input("Enter the number of your chosen ship type: "))
            if 1 <= choice <= len(SHIP_TYPES):
                return list(SHIP_TYPES.values())[choice - 1]
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Welcome, space pilot! Before we begin your adventure, let's set the stage.")
    player_name = input("What is your name? ")
    start_location, ship_name, description, ship_type = choose_starting_scenario()
    
    player = Player(player_name)
    ship = ShipStatus(ship_name, ship_type)
    universe = Universe(start_location)
    event_system = EventSystem()
    chat = ChatInterface(player_name, ship_name, description)

    print_instructions()
    print(f"\nAI: Welcome aboard the {ship_name}, a {ship_type.name} class vessel, {player_name}! You are currently a {description} in the {start_location}. How may I assist you today?")

    turn_counter = 0
    while True:
        turn_counter += 1
        print(f"\nShip Status: {ship.get_status_report()}")
        print(f"Location: {universe.get_current_location()}")
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("AI: Understood, pilot. Shutting down systems and ending the mission. Thank you for your service.")
            break
        elif user_input.lower() == 'help':
            print_instructions()
            continue

        event_info = event_system.check_for_events(player, ship, universe)
        ship_status = ship.get_status_report()
        nearby_ships = universe.get_nearby_ships_report()
        
        response = chat.send_message(user_input, ship_status, nearby_ships, event_info)
        print(f"AI: {response}")

        # Uncomment to see event info 
        # if event_info:
        #     print(f"\nEvent occurred:\n{event_info}")
        
        # Uncomment the following line for debugging the event probability
        # print(f"Debug: Current event probability: {event_system.current_probability:.4f}")

if __name__ == "__main__":
    main()