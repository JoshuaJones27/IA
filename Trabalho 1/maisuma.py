import heapq
import random

# A* algorithm to find the optimal parking spot for a ship
def a_star(ships, dock_1, dock_2):
    heap = []
    heapq.heappush(heap, (0, 0, dock_1))
    visited = set()
    while heap:
        time, ship_index, dock = heapq.heappop(heap)
        if dock in visited:
            continue
        visited.add(dock)
        if ship_index == len(ships) - 1:
            return time
        ship = ships[ship_index]
        if ship[2] == "large":
            dock = dock_2
        wait_time = max(0, dock[1] - ship[1])
        heapq.heappush(heap, (time + wait_time + ship[0], ship_index + 1, (dock[0], dock[1] + ship[0])))
    return float("inf")

# Genetic algorithm to find the optimal parking spot for a ship
def genetic(ships, dock_1, dock_2):
    import random
    import numpy as np
    population = [random.sample(range(len(ships)), len(ships)) for _ in range(100)]
    for _ in range(100):
        for individual in population:
            dock = dock_1
            wait_time = 0
            for i in individual:
                ship = ships[i]
                if ship[2] == "large":
                    dock = dock_2
                wait_time += max(0, dock[1] - ship[1])
                dock = (dock[0], dock[1] + ship[0])
            individual.append(wait_time)
        population = sorted(population, key=lambda x: x[-1])[:50]
        population = [random.sample(i[:-1], len(ships)) for i in population]
    return min(individual[-1] for individual in population)

# Example usage
#ships = [(10, 9, "small"), (5, 18, "large"), (15, 8, "small")]
# Generate 100 ship examples
ships = []
for i in range(100):
    time_spent = random.randint(1, 24) # time spent in dock between 1 and 24 hours
    arrival_time = random.randint(0, 24) # arrival time between 0 and 24 hours
    ship_size = random.choice(["small", "large"]) # randomly choose ship size
    ships.append((time_spent, arrival_time, ship_size))

dock_1 = ("dock 1", 8)
dock_2 = ("dock 2", 12)
print(a_star(ships, dock_1, dock_2))
print(genetic(ships, dock_1, dock_2))
