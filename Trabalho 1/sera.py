import random

class Ship:
    def __init__(self, name, ship_type, arrival_time, dock_time):
        self.name = name
        self.ship_type = ship_type
        self.arrival_time = arrival_time
        self.dock_time = dock_time
        self.waiting_time = 0
        
        # convert arrival_time to minutes
        self.arrival_time = arrival_time*60
        # convert dock_time to minutes
        self.dock_time = dock_time

class Dock:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.ships = []
        self.waiting_ships = []

    def add_ship(self, ship):
        if len(self.ships) < self.capacity:
            self.ships.append(ship)
        else:
            self.waiting_ships.append(ship)

def A_Star(ships, dock1, dock2, dock_time):
    for ship in ships:
        if ship.ship_type == "small":
            if len(dock1.ships) < 5:
                dock1.add_ship(ship)
                print(f"{ship.name} of size {ship.ship_type} has been assigned to {dock1.name} with waiting time of {ship.waiting_time} minutes")
            else:
                dock1.waiting_ships.append(ship)
                ship.waiting_time += dock_time
                print(f"{ship.name} of size {ship.ship_type} is waiting to be assigned to {dock1.name} with waiting time of {ship.waiting_time} minutes")
                for waiting_ship in dock1.waiting_ships:
                    waiting_ship.waiting_time += dock_time
        else:
            if len(dock2.ships) < 3:
                dock2.add_ship(ship)
                print(f"{ship.name} of size {ship.ship_type} has been assigned to {dock2.name} with waiting time of {ship.waiting_time} minutes")
                if ship in dock2.waiting_ships:
                    dock2.waiting_ships.remove(ship)
            else:
                    if (len(dock2.ships) == 2 and dock2.ships[0].ship_type == "small" and dock2.ships[1].ship_type == "small") or (len(dock2.ships) == 1 and dock2.ships[0].ship_type == "small"):
                        dock2.waiting_ships.append(ship)
                        ship.waiting_time += dock_time
                        print(f"{ship.name} of size {ship.ship_type} is waiting to be assigned to {dock2.name} with waiting time of {ship.waiting_time} minutes")
                    elif (len(dock2.ships) == 1 and dock2.ships[0].ship_type == "big") or (len(dock2.ships) == 2 and dock2.ships[0].ship_type == "big" and dock2.ships[1].ship_type == "big"):
                        dock2.waiting_ships.append(ship)
                        ship.waiting_time += dock_time
                        print(f"{ship.name} of size {ship.ship_type} is waiting to be assigned to {dock2.name} with waiting time of {ship.waiting_time} minutes")
                    else:
                        dock2.add_ship(ship)
                        print(f"{ship.name} of size {ship.ship_type} has been assigned to {dock2.name} with waiting time of {ship.waiting_time} minutes")
                    if ship in dock2.waiting_ships:
                        dock2.waiting_ships.remove(ship)
    return dock1, dock2


if __name__ == "__main__":
    dock1 = Dock("Dock 1", 5)
    dock2 = Dock("Dock 2", 3)
    ships = [Ship("Ship 1", "big", 8, 70), Ship("Ship 2", "small", 9, 100), Ship("Ship 3", "big", 10, 120), Ship("Ship 4", "small", 11, 200), 
    Ship("Ship 1", "big", 8, 70), Ship("Ship 2", "small", 9, 100), Ship("Ship 3", "big", 10, 120), Ship("Ship 4", "small", 11, 200), 
    Ship("Ship 1", "big", 8, 70), Ship("Ship 2", "small", 9, 100), Ship("Ship 3", "big", 10, 120), Ship("Ship 4", "small", 11, 200)]
    dock_time = 2
    A_Star(ships, dock1, dock2, dock_time)
    #dock1 = Dock("Dock 1", 5)
    #dock2 = Dock("Dock 2", 3)
    #Genetic(ships, dock1, dock2)

#if __name__ == "__main__":
#    dock1 = Dock("Dock 1", 5)
#    dock2 = Dock("Dock 2", 3)
#    ships = []
#    for i in range(100):
#        name = f"Ship {i+1}"
#        ship_type = random.choice(["big", "small"])
#        arrival_time = random.randint(8, 20)
#        dock_time = random.randint(1, 4)
#        ships.append(Ship(name, ship_type, arrival_time, dock_time))
#    dock_time = 2
#    A_Star(ships, dock1, dock2, dock_time)
#    dock1 = Dock("Dock 1", 5)
#    dock2 = Dock("Dock 2", 3)