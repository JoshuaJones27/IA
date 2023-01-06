# Represents a ship that is docked at the shipping dock
class Ship:
    def __init__(self, arrival_time, wait_time, port, ship_type):
        self.arrival_time = arrival_time
        self.wait_time = wait_time
        self.port = port
        self.ship_type = ship_type

# Represents a shipping dock
class Dock:
    def __init__(self, dock_number, max_ship_size):
        self.dock_number = dock_number
        self.max_ship_size = max_ship_size
        self.ships = []

    # Adds a ship to the dock
    def add_ship(self, ship):
        self.ships.append(ship)

# Sorts the ships in the list by their arrival time
def sort_ships_by_arrival_time(ships):
    return sorted(ships, key=lambda ship: ship.arrival_time)

# Optimizes the organization of the shipping docks
def optimize_dock(dock1, dock2, ships):
    # Sort the ships by their arrival time
    ships = sort_ships_by_arrival_time(ships)

    # Initialize the current time to the arrival time of the first ship
    current_time = ships[0].arrival_time

    # Iterate through the ships and add them to the docks
    for ship in ships:
        # Check if the ship can be added to dock 1
        if len(dock1.ships) < dock1.max_ship_size and (ship.ship_type != "big" or dock1.dock_number != 1):
            # Update the current time and add the ship to the dock
            current_time = max(current_time, ship.arrival_time) + ship.wait_time
            dock1.add_ship(ship)
        else:
            # Update the current time and add the ship to the dock
            current_time = max(current_time, ship.arrival_time) + ship.wait_time
            dock2.add_ship(ship)

    # Return the total wait time
    return current_time

# Example usage
dock1 = Dock(1, 3)
dock2 = Dock(2, 5)

ships = [
    Ship(0, 10, "Port A", "small"),
    Ship(0, 20, "Port B", "big"),
    Ship(5, 15, "Port C", "small"),
    Ship(10, 10, "Port D", "small"),
    Ship(15, 5, "Port E", "small")
]

total_wait_time = optimize_dock(dock1, dock2, ships)

print("Optimized shipping dock organization:")
print(f"Dock 1: {[ship.port for ship in dock1.ships]}")
print(f"Dock 2: {[ship.port for ship in dock2.ships]}")
print(f"Total wait time: {total_wait_time} minutes")



#fazer mais um algortimo greedy