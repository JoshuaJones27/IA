import random

class Ship:
    def __init__(self, name, size, arrival_time, dock_time, dock_num):
        self.name = name
        self.size = size # 1 for small, 2 for big
        self.arrival_time = arrival_time
        self.dock_time = dock_time
        self.dock_num = dock_num

class Dock:
    def __init__(self):
        self.dock1 = []
        self.dock2 = []
        self.waiting_ships = []
        self.time = 0
        
    def add_ship(self, ship):
        if ship.size == 1:
            if len(self.dock1) == 0:
                self.dock1.append(ship)
            elif len(self.dock2) == 0:
                self.dock2.append(ship)
            else:
                self.waiting_ships.append(ship)
        else:
            if len(self.dock2) == 0:
                self.dock2.append(ship)
            else:
                self.waiting_ships.append(ship)
                
    def update_time(self):
        self.time += 1
        for i, ship in enumerate(self.dock1):
            ship.dock_time -= 1
            if ship.dock_time == 0:
                self.dock1.pop(i)
        for i, ship in enumerate(self.dock2):
            ship.dock_time -= 1
            if ship.dock_time == 0:
                self.dock2.pop(i)
        if len(self.dock1) == 0 and len(self.waiting_ships) > 0:
            self.dock1.append(self.waiting_ships.pop(0))
        if len(self.dock2) == 0 and len(self.waiting_ships) > 0:
            self.dock2.append(self.waiting_ships.pop(0))

def a_star_algorithm(dock, ships):
    total_wait_time = 0
    for ship in ships:
        if ship.arrival_time > dock.time:
            dock.time = ship.arrival_time
        total_wait_time += dock.time - ship.arrival_time
        dock.add_ship(ship)
        while len(dock.waiting_ships) > 0:
            dock.update_time()
    return total_wait_time

def genetic_algorithm(dock, ships):
    total_wait_time = 0
    random.shuffle(ships)
    for ship in ships:
        if ship.arrival_time > dock.time:
            dock.time = ship.arrival_time
        total_wait_time += dock.time - ship.arrival_time
        dock.add_ship(ship)
        while len(dock.waiting_ships) > 0:
            dock.update_time()
    return total_wait
# Create 100 ships
ships = []
for i in range(100):
    name = "Ship " + str(i)
    size = random.randint(1, 2) # Randomly assign size of ship
    arrival_time = random.randint(0, 1440) # Randomly assign arrival time between 0 and 1440 (24 hours)
    dock_time = random.randint(60, 240) # Randomly assign dock time between 60 and 240 minutes
    dock_num = random.randint(1, 2) # Randomly assign dock number
    ships.append(Ship(name, size, arrival_time, dock_time, dock_num))

# Create a dock
dock = Dock()

# Use A* algorithm to optimize wait time
a_star_wait_time = a_star_algorithm(dock, ships)
print("Total wait time using A* algorithm:", a_star_wait_time, "minutes")

# Use genetic algorithm to optimize wait time
genetic_wait_time = genetic_algorithm(dock, ships)
print("Total wait time using genetic algorithm:", genetic_wait_time, "minutes")

# Compare the results and choose the best algorithm
if a_star_wait_time < genetic_wait_time:
    print("A* algorithm is better.")
else:
    print("Genetic algorithm is better.")
