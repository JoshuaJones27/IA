import heapq

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

# Represents the state of the shipping dock organization at a given time
class State:
    def __init__(self, dock1, dock2, time):
        self.dock1 = dock1
        self.dock2 = dock2
        self.time = time

    # Calculates the estimated waiting time for all ships at the dock
    def estimate_total_wait_time(self):
        total_wait_time = 0
        for ship in self.dock1.ships:
            total_wait_time += ship.wait_time
        for ship in self.dock2.ships:
            total_wait_time += ship.wait_time
        return total_wait_time

    # Returns the next possible states from the current state
    def get_next_states(self):
        next_states = []

        # Check if a ship can be removed from dock 1
        if len(self.dock1.ships) > 0:
            next_dock1 = Dock(self.dock1.dock_number, self.dock1.max_ship_size)
            next_dock1.ships = self.dock1.ships[1:]
            next_dock2 = Dock(self.dock2.dock_number, self.dock2.max_ship_size)
            next_dock2.ships = self.dock2.ships[:]
            next_states.append(State(next_dock1, next_dock2, self.time + self.dock1.ships[0].wait_time))

        # Check if a ship can be removed from dock 2
        if len(self.dock2.ships) > 0:
            next_dock1 = Dock(self.dock1.dock_number, self.dock1.max_ship_size)
            next_dock1.ships = self.dock1.ships[:]
            next_dock2 = Dock(self.dock2.dock_number, self.dock2.max_ship_size)
            next_dock2.ships = self.dock2.ships[1:]
            next_states.append(State(next_dock1, next_dock2, self.time + self.dock2.ships[0].wait_time))

        # Check if a ship can be added to dock 1
        for ship in self.dock1.ships:
            if ship.arrival_time > self.time:
              break
            if ship.ship_type != "big" and len(self.dock1.ships) < self.dock1.max_ship_size:
                next_dock1 = Dock(self.dock1.dock_number, self.dock1.max_ship_size)
                next_dock1.ships = self.dock1.ships[:] + [ship]
                next_dock2 = Dock(self.dock2.dock_number, self.dock2.max_ship_size)
                next_dock2.ships = self.dock2.ships[:]
                next_states.append(State(next_dock1, next_dock2, self.time))

        # Check if a ship can be added to dock 2
        for ship in self.dock2.ships:
            if ship.arrival_time > self.time:
                break
            if len(self.dock2.ships) < self.dock2.max_ship_size:
                next_dock1 = Dock(self.dock1.dock_number, self.dock1.max_ship_size)
                next_dock1.ships = self.dock1.ships[:]
                next_dock2 = Dock(self.dock2.dock_number, self.dock2.max_ship_size)
                next_dock2.ships = self.dock2.ships[:] + [ship]
                next_states.append(State(next_dock1, next_dock2, self.time))
            return next_states

    def optimize_dock(dock1, dock2, ships):
        # Add the initial state to the priority queue
        initial_state = State(dock1, dock2, 0)
        priority_queue = []
        heapq.heappush(priority_queue, (initial_state.estimate_total_wait_time(), initial_state))

        while len(priority_queue) > 0:
            # Get the state with the lowest estimated wait time
            current_state = heapq.heappop(priority_queue)

        # Check if the current state is a solution
        if len(current_state.dock1.ships) == 0 and len(current_state.dock2.ships) == 0:
           return current_state

    # Add the next possible states to the priority queue
        for next_state in current_state.get_next_states():
            heapq.heappush(priority_queue, (next_state.estimate_total_wait_time(), next_state))


dock1 = Dock(1, 3)
dock2 = Dock(2, 5)

ships = [
Ship(0, 10, "Port A", "small"),
Ship(0, 20, "Port B", "big"),
Ship(5, 15, "Port C", "small"),
Ship(10, 10, "Port D", "small"),
Ship(15, 5, "Port E", "small")
]

optimal_state = State.optimize_dock(dock1, dock2, ships)

print("Optimal shipping dock organization:")
print(f"Dock 1: {[ship.port for ship in optimal_state.dock1.ships]}")
print(f"Dock 2: {[ship.port for ship in optimal_state.dock2.ships]}")
print(f"Total wait time: {optimal_state.time} minutes")