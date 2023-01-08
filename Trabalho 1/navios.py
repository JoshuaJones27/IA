import heapq
import random

class Ship:
    def __init__(self, arrival_time, wait_time, port, ship_type):
        self.arrival_time = arrival_time
        self.wait_time = wait_time
        self.port = port
        self.ship_type = ship_type

class Dock:
    def __init__(self, name, capacity, ship_types):
        self.name = name
        self.capacity = capacity
        self.ship_types = ship_types

def get_shortest_wait_time(docks, ships):
    # Initialize variables
    heap = []
    visited = set()
    g = {dock: float('inf') for dock in docks}
    f = {dock: float('inf') for dock in docks}
    came_from = {dock: None for dock in docks}
    current = None

    # Add starting dock to the heap
    start_dock = docks[0]
    g[start_dock] = 0
    f[start_dock] = g[start_dock] + h(start_dock, ships)
    heapq.heappush(heap, (f[start_dock], start_dock))

    while heap:
        current = heapq.heappop(heap)[1]
        visited.add(current)

        # Check if we have reached the goal
        if is_goal(current, ships):
            return reconstruct_path(came_from, current)

        # Generate successors
        successors = generate_successors(current, docks, ships)
        for dock in successors:
            if dock in visited:
                continue
            tentative_g = g[current] + cost(current, dock, ships)
            if tentative_g < g[dock]:
                came_from[dock] = current
                g[dock] = tentative_g
                f[dock] = g[dock] + h(dock, ships)
                if dock not in heap:
                    heapq.heappush(heap, (f[dock], dock))

    return []

def generate_successors(dock, docks, ships):
    successors = []
    for other_dock in docks:
        if other_dock != dock and can_transfer(dock, other_dock, ships):
            successors.append(other_dock)
    return successors

def can_transfer(dock1, dock2, ships):
    if dock1.capacity < len(ships) or dock2.capacity < len(ships):
        return False
    if dock1.name == 'Dock 1' and 'Big Ship' in [s.ship_type for s in ships]:
        return False
    return True

def cost(dock1, dock2, ships):
    transfer_time = 30
    return transfer_time + sum([s.wait_time for s in ships if s.port == dock2.name])

def h(dock, ships):
    return sum([s.wait_time for s in ships if s.port == dock.name])

def is_goal(dock, ships):
    return all(s.port == dock.name for s in ships)

def reconstruct_path(came_from, current):
    total_path = [current]
    while came_from[current] is not None:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

def genetic_algorithm(docks, ships, population_size=100, num_generations=100):
    def create_chromosome(docks):
        return [random.choice(docks) for _ in ships]

    def create_initial_population(docks, population_size):
        return [create_chromosome(docks) for _ in range(population_size)]

    def get_fitness(chromosome):
        wait_time = 0
        for i, dock in enumerate(chromosome):
            if i > 0:
                wait_time += 30
            wait_time += sum(s.wait_time for s in ships if s.port == dock.name)
        return -wait_time

    def get_best_chromosome(population, docks, ships):
        return max(population, key=lambda x: get_fitness(x))

    def mutate(chromosome, docks):
        mutant = chromosome[:]
        i = random.randint(0, len(mutant) - 1)
        mutant[i] = random.choice(docks)
        return mutant

    def crossover(chromosome1, chromosome2):
        i = random.randint(1, len(chromosome1) - 1)
        return chromosome1[:i] + chromosome2[i:]

    population = create_initial_population(docks, population_size)
    best_chromosome = get_best_chromosome(population, docks, ships)
    for _ in range(num_generations):
        next_population = []
        while len(next_population) < population_size:
            chromosome1 = random.choice(population)
            chromosome2 = random.choice(population)
            if random.random() < 0.8:
                chromosome1 = mutate(chromosome1, docks)
            if random.random() < 0.8:
                chromosome2 = mutate(chromosome2, docks)
            next_population.append(crossover(chromosome1, chromosome2))
        population = next_population
        best_chromosome = get_best_chromosome(population, docks, ships)
    return best_chromosome

def main():
    # Create docks
    dock1 = Dock('Dock 1', 2, ['All'])
    dock2 = Dock('Dock 2', 2, ['All'])
    docks = [dock1, dock2]

    # Create ships
    ship1 = Ship(10, 20, 'Dock 1', 'Small Ship')
    ship2 = Ship(20, 30, 'Dock 2', 'Big Ship')
    ship3 = Ship(30, 40, 'Dock 2', 'Small Ship')
    ship4 = Ship(40, 50, 'Dock 1', 'Big Ship')
    ships = [ship1, ship2, ship3, ship4]

    # Organize shipping dock using A* algorithm
    a_star_solution = get_shortest_wait_time(docks, ships)
    print(f'A* Solution: {[dock.name for dock in a_star_solution]}')

    # Organize shipping dock using genetic algorithm
    genetic_algorithm_solution = genetic_algorithm(docks, ships)
    print(f'Genetic Algorithm Solution: {[dock.name for dock in genetic_algorithm_solution]}')

if __name__ == '__main__':
    main()
