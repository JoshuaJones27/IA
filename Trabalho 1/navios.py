#Code 1
# Create a class representing the shipping dock
class ShippingDock:
  def __init__(self):
    # Initialize the dock with two docking places
    self.docking_places = [None, None]

  def add_ship(self, ship):
    # Find the first available docking place
    for i, place in enumerate(self.docking_places):
      if place is None:
        # Assign the ship to the docking place
        self.docking_places[i] = ship
        # Calculate the wait time for the ship
        wait_time = 0
        for other_ship in self.docking_places:
          if other_ship is not None and other_ship.size > ship.size:
            wait_time += other_ship.loading_time
        return wait_time

# Create a class representing a ship
class Ship:
  def __init__(self, size, loading_time):
    self.size = size
    self.loading_time = loading_time

# Initialize a shipping dock
dock = ShippingDock()

# Create some ships
ship1 = Ship(size=1, loading_time=10)
ship2 = Ship(size=2, loading_time=5)

# Add the ships to the dock and print their wait times
print(dock.add_ship(ship1)) # 0 minutes
print(dock.add_ship(ship2)) # 10 minutes


#Code 2

# define the number of docks at the port
NUM_DOCKS = 2

# define the maximum size of ships that can dock at the second dock
SECOND_DOCK_MAX_SIZE = 1000

# define a class to represent a ship
class Ship:
  def __init__(self, arrival_time, loading_time, ship_size):
    self.arrival_time = arrival_time
    self.loading_time = loading_time
    self.ship_size = ship_size

# define a class to represent the shipping dock
class ShippingDock:
  def __init__(self):
    # create a queue to hold ships that are waiting to dock
    self.waiting_ships = []
    # create a list to hold the ships that are currently docked
    self.docked_ships = []
  
  # a function to add a ship to the queue
  def add_ship_to_queue(self, ship):
    self.waiting_ships.append(ship)
  
  # a function to dock a ship at an available dock
  def dock_ship(self, ship):
    # if there is an available dock, dock the ship
    if len(self.docked_ships) < NUM_DOCKS:
      self.docked_ships.append(ship)
    # if there is no available dock, add the ship to the queue
    else:
      self.add_ship_to_queue(ship)
  
  # a function to update the status of the docked ships
  def update_docked_ships(self):
    # iterate over the docked ships
    for ship in self.docked_ships:
      # if the ship's loading time has elapsed, undock the ship
      if ship.loading_time == 0:
        self.docked_ships.remove(ship)
      # if the ship is still loading, decrement its loading time
      else:
        ship.loading

#Code 3

# This represents the port with two docking places
class Port:
  def __init__(self):
    self.docking_places = [None, None]

  # Try to park a ship in a docking place.
  # Returns the docking place index if successful, or None if there is no available space.
  def try_park_ship(self, ship):
    # Check if the ship can park in the first docking place
    if self.docking_places[0] is None and not ship.requires_second_dock:
      self.docking_places[0] = ship
      return 0

    # Check if the ship can park in the second docking place
    if self.docking_places[1] is None:
      self.docking_places[1] = ship
      return 1

    # No available docking places
    return None

  # Unpark a ship from a docking place
  def unpark_ship(self, docking_place_index):
    self.docking_places[docking_place_index] = None


# This represents a ship that arrives at the port
class Ship:
  def __init__(self, arrival_time, loading_time, requires_second_dock):
    self.arrival_time = arrival_time
    self.loading_time = loading_time
    self.requires_second_dock = requires_second_dock

  # This method is called when the ship arrives at the port
  def arrive_at_port(self, port):
    # Try to park the ship
    docking_place_index = port.try_park_ship(self)

    # If there is no available space, wait until there is one
    while docking_place_index is None:
      # Wait for one minute
      time.sleep(60)

      # Try to park the ship again
      docking_place_index = port.try_park_ship(self)

    # The ship has successfully parked, now start loading/unloading
    time.sleep(self.loading_time * 60)

    # The ship is done, unpark it from the docking place

#Code 4

# Define the types of ships that can be parked at the second dock
BIG_SHIPS = ["oil tanker", "container ship"]

# Define the maximum number of docking places at the port
MAX_DOCKS = 2

# Create a list of ships at the dock
ships_at_dock = []

# Create a queue of ships waiting to dock
ships_waiting = []

class Ship:
    def __init__(self, name, arrival_time, time_in_dock, ship_type):
        self.name = name
        self.arrival_time = arrival_time
        self.time_in_dock = time_in_dock
        self.ship_type = ship_type
    
    # Define a method for the ship to dock at the port
    def dock(self):
        # Check if there is an available dock
        if len(ships_at_dock) < MAX_DOCKS:
            # If there is, add the ship to the list of ships at the dock
            ships_at_dock.append(self)
            print(f"{self.name} has docked at the port.")
        else:
            # If there isn't, add the ship to the queue of ships waiting to dock
            ships_waiting.append(self)
            print(f"{self.name} is waiting to dock at the port.")
            
    # Define a method for the ship to leave the dock
    def leave_dock(self):
        # Remove the ship from the list of ships at the dock
        ships_at_dock.remove(self)
        print(f"{self.name} has left the dock.")
        
        # Check if there are any ships waiting to dock
        if len(ships_waiting) > 0:
            # If there are, get the first ship in the queue and dock it
            next_ship = ships_waiting.

#Code 5

# A queue to keep track of the ships waiting at the dock
ship_queue = []

# A list to keep track of the ships that are currently loading/unloading
docked_ships = []

# The time when the last ship started loading/unloading
last_time = 0

# The number of docking places in the port
number_of_docking_places = 2

# A dictionary to keep track of the estimated wait time for each ship
wait_times = {}

# Function to simulate the arrival of a ship at the dock
def arrive(ship, time, loading_time, type):
  global ship_queue
  global docked_ships
  global last_time
  global wait_times

  # If the ship has to dock in the second place and the second place is not available,
  # the ship has to wait
  if type == "big" and len(docked_ships) == number_of_docking_places - 1:
    ship_queue.append((ship, time, loading_time, type))
    return

  # If the ship has to dock in the second place and the second place is available,
  # the ship can start loading/unloading immediately
  if type == "big" and len(docked_ships) < number_of_docking_places - 1:
    last_time = time
    docked_ships.append((ship, time, loading_time, type))
    wait_times[ship] = 0
    return

  # If the ship has to dock in the first place and there are no ships currently loading/unloading,
  # the ship can start loading/unloading immediately
  if len(docked_ships) == 0:
    last_time = time
    docked_ships.append((ship, time, loading_time, type))
    wait_times[ship] = 0
    return

  # If the ship has to dock in the first place and there is at least one ship currently loading/unloading,
  # the ship has to wait
  if len(docked_ships) > 0:
    ship_queue
