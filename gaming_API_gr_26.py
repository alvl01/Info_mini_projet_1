import gaming_tools
import time
import random

# Game documentation
def help_game():
	"""Explain how to use the functions of this game.
	"""
	print("First of all, use init_game() to initialise the game by creating the 'Aldebaran' and 'Epsilon Aurigae' planets")
	print("\nAvailable functions :\n")

	print("1. create_planet(planet_name) - Create a new planet with the given name.") #done
	print("2. planet_state(planet_name) - Display information about the planet")

	print("3. create_ship(ship_name) - Create a new ship with the given name.")
	print("4. ship_state(planet_name) - Display information about the ship")
	print("5. ship_is_ready(ship_name) - Check if the ship is ready to move")
	print("6. move_ship(ship_name, destination_planet) - Move the ship to the destination planet.")
	print("7. upgrade_ship(ship_name, upgrade) - Improve the speed of the ship.")
	print("8. repair_ship(ship_name) - Repaire the ship when it's broken using the resources of the current planet.")

	print("9. get_distance(ship_name, planet_name) - Get the distance between ship and the planet.")
	print("10. reset_game() - Reset the game (prepare for a new game)")
	
	print("Basic usage:")
	print('move_ship("group 26 ship", "planet oranus")')
	print('And so on .. Enjoy! ^_^')



# Init the game for the first time
def init_game():
	"""Initialise the game by creating the two basic planets "Aldebaran" and "Epsilon Aurigae"
	"""
	create_planet("Aldebaran", 0, 0)
	create_planet("Epsilon Aurigae", 1000, 1000)
	gaming_tools.set_planet_resources("Aldebaran", 0)
	gaming_tools.set_planet_resources("Epsilon Aurigae", 0)
	print("planet Aldebaran and Epsilon Aurigae have been created and set to 0")
	print("Everything is correctly set up, you can start creating planets and ships and enjoy the game!")





def create_planet(name, coord_x, coord_y):
	"""Create a new planet with a given name

	Parameters
	----------
	name: name of the planet (str)
	coord_x: x coordinate of the planet (int)
	coord_y: y coordinate of the planet (int)
	"""

	if gaming_tools.planet_exists(name):
		print("Error, the planet name already used!")
		return
	if coord_x > 1000 or coord_y > 1000 or coord_x < 0 or coord_y < 0:
		print("Error, the coordinates are not between 0 and 1000!")
		return

	ressources = random.randint(5, 20)

	gaming_tools.add_new_planet(name, ressources)
	gaming_tools.set_planet_location(name, coord_x, coord_y)
	print("The planet %s has been created" % name)





def planet_state(planet):
	"""Display informations about the planet

	Parameters
	----------
	planet: name of the planet (str)
	"""

	if not gaming_tools.planet_exists(planet):
		print("Error, the planet doesn't exist!")
		return
	location = gaming_tools.get_planet_location(planet)
	resources = gaming_tools.get_planet_resources(planet)
	print("the planet is in location: %s and have %d resources" %(location, resources))





def create_ship(name):
	"""Create a new ship with a given name

	Parameters
	----------
	name: name of the ship (str)

	"""
	if not gaming_tools.planet_exists("Aldebaran"):
		print("Error, Aldebaran is not created yet!")
		return
	if gaming_tools.ship_exists(name):
		print("Error, the ship name already used!")
		return
	
	gaming_tools.add_new_ship(name, 1, False)
	gaming_tools.set_ship_location(name, "Aldebaran")
	print("The ship %s has been created" % name)

def ship_state(ship):
	"""Diplay information about the ship

	Parameters
	----------
	ship: name of the ship (str)
	"""
	if not gaming_tools.ship_exists(ship):
		print("Error, the ship doesn't exist!")
		return
	loc = gaming_tools.get_ship_location(ship)
	speed = gaming_tools.get_ship_speed(ship)
	broken = gaming_tools.is_ship_broken(ship)
	ready = gaming_tools.get_when_ship_is_ready(ship)
	print("Location : %s" % loc)
	print("Speed : %d parsec/sec" % speed)
	print(("Ship is broken" if broken else "ship is not broken!"))
	print("Ship is ready" if ship_is_ready(ship) else "ship is not ready wait " + text_time(ready - time.time()) + "s")


def ship_is_ready(ship):
	"""Check if the ship is ready to move

	Parameters
	----------
	ship: name of the ship (str)

	Returns
	-------
	status: True of it's ready, False otherwise (bool)
	"""

	if not gaming_tools.ship_exists(ship):
		print("Error, the ship doesn't exist!")
		return

	return gaming_tools.get_when_ship_is_ready(ship) < time.time()





def move_ship(ship, planet):
	"""Move the ship

	Parameters
	----------
	ship: name of the ship (str)
	planet: name of planet where you want to go (str)
	"""

	if not gaming_tools.ship_exists(ship):
		print("Error, the ship doesn't exist!")
		return
	if not gaming_tools.planet_exists(planet):
		print("Error, the planet doesn't exist!")
		return
	if gaming_tools.is_ship_broken(ship):
		print("Error, the ship is broken, You cannot move it!")
		return
	if not ship_is_ready(ship):
		print("Error, the ship is not ready yet!")
		return
	
	# change position of the ship
	ship_speed = gaming_tools.get_ship_speed(ship)
	distance = get_distance(ship, planet)
	deltatime = int(distance / ship_speed)
	gaming_tools.set_ship_location(ship, planet)

	# is the ship broken
	if not random.randint(0, 2):
		gaming_tools.set_ship_broken(ship, True)

	# display the time
	print("you will land in ", text_time(deltatime))

	# set waiting time
	gaming_tools.set_when_ship_is_ready(ship, time.time() + deltatime)

def upgrade(ship, upgrade):
	"""Uprade the ship
	
	Parameters
	----------
	ship: name of the ship (str)
	upgrade: velocity added (int)
	"""

	if not gaming_tools.ship_exists(ship):
		print("Error, the ship doesn't exist")
		return
	if gaming_tools.is_ship_broken(ship):
		print("Error, the ship is broken, you cannot upgrate it!")
		return
	if not ship_is_ready(ship):
		print("Error, the ship is not ready yet!")
		return
	planet = gaming_tools.get_ship_location(ship)

	planet_resources = gaming_tools.get_planet_resources(planet)
	if planet_resources < upgrade:
		print("Error, this planet does not have sufficient resources to upgrade the ship")
		return
	
	gaming_tools.set_planet_resources(planet, planet_resources - upgrade)

	speed = gaming_tools.get_ship_speed(ship) + upgrade
	gaming_tools.set_ship_speed(ship, speed)
	upgrade_time = 40 * (upgrade**2)

	print("Ship is upgrading ... Please wait for %d seconds" % (int(upgrade_time)))

	gaming_tools.set_when_ship_is_ready(ship, time.time() + upgrade_time)

def repair(ship):
	"""Repair the ship

	Parameters
	----------
	ship: name of the ship (str)
	"""

	if not gaming_tools.ship_exists(ship):
		print("Error, the ship doesn't exist")
		return
	if not gaming_tools.is_ship_broken(ship):
		print("Error, the ship is broken, you cannot repair it")
		return
	if not ship_is_ready(ship):
		print("Error, the ship is not ready yet!")
		return
	
	planet = gaming_tools.get_ship_location(ship)
	planet_resources = gaming_tools.get_planet_resources(planet)

	if(planet_resources < 3) :
		print("Error, this planet does not have sufficient resources to repair the ship")
		return
	
	ship_speed = gaming_tools.get_ship_speed(ship) 
	repaire_time = 20 * ship_speed

	print("Ship is under repair ... Please wait for %d seconds" % (int(repaire_time)))

	gaming_tools.set_when_ship_is_ready(ship, time.time() + repaire_time)
	gaming_tools.set_ship_broken(ship, False)
	gaming_tools.set_planet_resources(planet, planet_resources - 3)

def get_distance(ship, planet):
	"""Calculate the distance between ship and planet

	Parameters
	----------
	ship: name of the ship (str)
	planet: name of the planet (str)

	Returns
	-------
	distance: distance ship planet(float)
	"""
	if not gaming_tools.ship_exists(ship):
		print("Error, the ship doesn't exist!")
		return
	if not gaming_tools.planet_exists(planet):
		print("Error, the planet doesn't exist!")
		return
	ship_x, ship_y = gaming_tools.get_planet_location(gaming_tools.get_ship_location(ship))
	planet_x, planet_y = gaming_tools.get_planet_location(planet)
	return ((ship_x - planet_x) ** 2 + (ship_y - planet_y) ** 2) ** (1/2)

def text_time(time):
	"""Return the time in format "x min y s"

	Parameters
	----------
	time: a time to format (int)

	Returns
	------
	fomated_time: formated time(str)
	"""
	return ("" if time // 60 == 0 else str(time // 60) + "min ") + str(time % 60) + "s"
  
def reset_game():
	"""Reset the game (prepare for a new game)
	"""
	gaming_tools.reset_game()
	print("The game has been reset!")
	print("You can start a new round just by executing init_game()")

	return