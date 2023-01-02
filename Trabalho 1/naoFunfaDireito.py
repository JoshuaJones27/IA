import heapq

class Ship:
    def __init__(self, arrival_time, wait_time, port, ship_type):
        self.arrival_time = arrival_time
        self.wait_time = wait_time
        self.port = port
        self.ship_type = ship_type

class Dock:
    def __init__(self, id, max_capacity, accepts_big_ships):
        self.id = id
        self.max_capacity = max_capacity
        self.accepts_big_ships = accepts_big_ships
        self.current_capacity = 0
        self.ships = []

def get_estimated_wait_time(dock, ship):
    # Calculate the total waiting time for the ship at the given dock
    total_wait_time = 0
    for s in dock.ships:
        total_wait_time += s.wait_time
    return total_wait_time + ship.wait_time

def a_star(docks, ship):
    # Create a priority queue for the A* algorithm
    queue = []
    # Add the first dock as the starting point
    heapq.heappush(queue, (0, docks[0]))
    # Keep track of the visited docks
    visited = set()

    while queue:
        # Get the dock with the smallest estimated waiting time
        total_wait_time, dock = heapq.heappop(queue)

        # Check if the dock is a valid destination for the ship
        if dock.accepts_big_ships or ship.ship_type != 'big':
            if dock.current_capacity < dock.max_capacity:
                # The ship can dock at this dock, so return the total waiting time
                return total_wait_time

        # Mark the dock as visited
        visited.add(dock)

        # Add the neighboring docks to the queue
        for neighbor in docks:
            if neighbor not in visited:
                # Calculate the estimated waiting time for the ship at this dock
                estimated_wait_time = get_estimated_wait_time(neighbor, ship)
                # Add the dock to the queue with the estimated waiting time as the priority
                heapq.heappush(queue, (estimated_wait_time, neighbor))

    # No valid dock was found for the ship
    return -1

def main():
    # Initialize the docks
    docks = [Dock(1, 5, False), Dock(2, 10, True)]
    # Initialize the ships
    ships = [Ship(9, 60, 'A', 'big'), Ship(10, 30, 'B', 'small'), Ship(11, 45, 'C', 'small')]

    # Optimize the organization of the shipping docks
    for ship in ships:
        wait_time = a_star(docks, ship)
        if wait_time == -1:
            print(f'No valid dock found for ship {ship.ship_type} from port {ship.port}')
        else:
            print(f'Ship {ship.ship_type} from port {ship.port} can dock at dock {docks[0].id} with a wait time of {wait_time} minutes')

if __name__ == '__main__':
    main()  