import heapq

class Ship:
    def __init__(self, arrival_time, wait_time, port, ship_type):
        self.arrival_time = arrival_time
        self.wait_time = wait_time
        self.port = port
        self.ship_type = ship_type

class Dock:
    def __init__(self, id, max_size):
        self.id = id
        self.max_size = max_size
        self.ships = []
    
    def add_ship(self, ship):
        self.ships.append(ship)
    
    def remove_ship(self, ship):
        self.ships.remove(ship)
    
    def get_wait_time(self):
        wait_time = 0
        for ship in self.ships:
            wait_time += ship.wait_time
        return wait_time

class State:
    def __init__(self, docks, f=0, g=0):
        self.docks = docks
        self.f = f
        self.g = g
    
    def __lt__(self, other):
        return self.f < other.f

def a_star(start, goal, ships):
    closed_set = set()
    open_set = []
    heapq.heappush(open_set, start)
    
    while open_set:
        current = heapq.heappop(open_set)
        if current == goal:
            return current
        
        closed_set.add(current)
        
        for ship in ships:
            if ship.arrival_time > current.docks[0].get_wait_time() + current.docks[1].get_wait_time():
                continue
            for dock in current.docks:
                if (ship.port == dock.id or dock.id == 2) and (ship.ship_type != "big" or dock.id == 2):
                    new_docks = list(current.docks)
                    new_docks[dock.id - 1].add_ship(ship)
                    new_state = State(new_docks, current.g + ship.wait_time, current.g + ship.wait_time)
                    if new_state not in closed_set:
                        heapq.heappush(open_set, new_state)
    
    return None

def organize_docks(ships):
    dock1 = Dock(1, float("inf"))
    dock2 = Dock(2, float("inf"))
    start = State([dock1, dock2])
    goal = State([dock1, dock2], float("inf"))
    
    solution = a_star(start, goal, ships)
    
    if solution:
        print("Optimal solution found with wait time:", solution.f)
        for dock in solution.docks:
            print("Dock", dock.id)
            for ship in dock.ships:
                print("  Ship", ship.ship_type, "arrived at", ship.arrival_time, "with wait time", ship.wait_time)
    else:
        print("No solution found")

# Test with some ships
ships = [    Ship(10, 5, 1, "small"),    Ship(10, 3, 1, "big"),    Ship(12, 4, 2, "small"),    Ship(13, 5, 1, "medium"),    Ship(14, 2, 2, "big"),    Ship(15, 6, 1, "small")]

organize_docks(ships)
