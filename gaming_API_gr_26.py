import gaming_tools
import time
import random

## info
def help_game():#jugurtha
	"""Explain how to use the functions of this game.
	"""
	print("Available functions :")
	print("1. create_planet(planet_name) - Create a new planet with the given name.")
	print("2. create_ship(ship_name) - Create a new ship with the given name.")
	print("3. move_ship(ship_name, destination_planet) - Move the ship to the destination planet.")
	print("4. upgrade_ship(ship_name, planet_name) - Improve the speed of the ship.")
	print("5. repair_ship(ship_name, planet_name) - Repaire the ship when it's broken using the resources of the current planet.")
	print("6. get_distance(ship_name, planet_name) - Get the distance between ship and the planet.")
	print("7. planet_state(planet_name) - Display information about the planet")
	print("8. ship_state(planet_name) - Display information about the ship")
	

	print("\nExample usage:")
	print('move_ship("MyShip", "NewPlanet")')
	print('\nAnd so on ..')

def init_game():

	create_planet("Aldebaran", 0, 0)
	create_planet("Epsilon Aurigae", 1000, 1000)
	gaming_tools.set_planet_resources("Aldebaran", 0)
	gaming_tools.set_planet_resources("Epsilon Aurigae", 0)
	print("planet Aldebaran and Epsilon Aurigae have been created and set to 0")

def ship_state(ship):#anderson
	"""Diplay information about the ship

	Parameters
	----------
	ship: name of the ship (str)
	"""
	if not gaming_tools.ship_exists(ship):
		error(1)
		return
	loc = gaming_tools.get_ship_location(ship)
	speed = gaming_tools.get_ship_speed(ship)
	broken = gaming_tools.is_ship_broken(ship)
	ready = gaming_tools.get_when_ship_is_ready(ship)
	print("Location %s" % loc)
	print("Speed: %d parsec/sec" % speed)
	print(("Ship is broken" if broken else "ship is not broken!"))
	print("Ship is ready" if ship_is_ready(ship) else "ship is not ready wait " + text_time(ready - time.time()) + "s")

def ship_is_ready(ship):
	return gaming_tools.get_when_ship_is_ready(ship) < time.time()

# planet ressource et planet postion on ete combiné
def planet_state(planet):#ammar#abdelaziz
	"""Display information about the planet

	Parameters
	----------
	planet: name of the planet (str)
	"""
	if not gaming_tools.planet_exists(planet):
		error(2)
		return
	location = gaming_tools.get_planet_location(planet)
	resources = gaming_tools.get_planet_resources(planet)
	print("the planet is in location x: %s and have %d resources" %(location, resources))

def get_distance(ship, planet):
	"""Calculate the distance between ship and planet

	Parameters
	----------
	ship: name of the ship (str)
	planet: name of the planet (str)

	Returns
	------
	distance: distance ship planet(float)
	"""
	if not gaming_tools.ship_exists(ship):
		error(1)
		return
	if not gaming_tools.planet_exists(planet):
		error(2)
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

## Action

def move(ship, planet):#Alessandro
	"""Move the ship

	Parameters
	----------
	ship: name of the ship (str)
	planet: name of planet where you want to go (str)
	"""
	if not gaming_tools.ship_exists(ship):
		error(1)
		return
	if not gaming_tools.planet_exists(planet):
		error(2)
		return
	if gaming_tools.is_ship_broken(ship):
		error(5)
		return
	if not ship_is_ready(ship):
		error(6)
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

def upgrade_ship(ship, upgrade):#abdelaziz
	"""Uprade the ship
	
	Parameters
	----------
	ship: name of the ship (str)
	upgrade: velocity added (int)
	"""
	if not gaming_tools.ship_exists(ship):
		error(1)
		return
	if gaming_tools.is_ship_broken(ship):
		error(7)
		return
	if not ship_is_ready(ship):
		error(6)
		return
	planet = gaming_tools.get_ship_location(ship)
	if gaming_tools.get_planet_resources(planet) < upgrade:
		error(8)
		return
	speed = gaming_tools.get_ship_speed(ship) + upgrade
	gaming_tools.set_ship_speed(ship, speed)
	upgrade_time = 40 * (upgrade**2)
	print("Ship is upgrading ... Please wait for %d seconds" % (int(upgrade_time)))
	gaming_tools.set_when_ship_is_ready(ship, time.time() + upgrade_time)

def repair(ship): #jugurtha
	"""Repare the ship

	Parameters
	----------
	ship: name of the ship (str)
	"""
	if not gaming_tools.ship_exists(ship):
		error(1)
		return
	if not gaming_tools.is_ship_broken(ship):
		error(9)
		return
	if not ship_is_ready(ship):
		error(6)
		return
	planet = gaming_tools.get_ship_location(ship)
	planet_resources = gaming_tools.get_planet_resources(planet)
	if(planet_resources < 3) :
		error(8)
		return
	ship_speed = gaming_tools.get_ship_speed(ship) 
	repaire_time = 20 * ship_speed

	print("Ship is under repair ... Please wait for %d seconds" % (int(repaire_time)))
	gaming_tools.set_when_ship_is_ready(ship, time.time() + repaire_time)

	gaming_tools.set_ship_broken(ship, False)

	gaming_tools.set_planet_resources(planet, planet_resources - 3)



	
       

def create_planet(name, coord_x, coord_y):#anderson
	"""Create a planet

	Parameters
	----------
	name: name of the planet (str)
	coord_x: x coordinate of the planet (int)
	coord_y: y coordinate of the planet (int)
	"""
	if gaming_tools.planet_exists(name):
		error(4)
		return
	if coord_x > 1000 or coord_y > 1000 or coord_x < 0 or coord_y < 0:
		error(10)
		return

	ressources = random.randint(5, 20)

	gaming_tools.add_new_planet(name, ressources)
	gaming_tools.set_planet_location(name, coord_x, coord_y)
	print("the planet has been created")

def create_ship(name):#ammar
	"""Create a ship

	Parameters
	----------
	name: name of the ship (str)
	"""
	if not gaming_tools.planet_exists("Aldebaran"):
		error(11)
		return
	if gaming_tools.ship_exists(name):
		error(3)
		return
	gaming_tools.add_new_ship(name, 1, False)
	gaming_tools.set_ship_location(name, "Aldebaran")
	print("the ship has been created")

def error(value):# everyone just add error that you need
	"""Display error to the user

	Parameters
	----------
	value: error number (int)
	"""
	if value == 1:
		print("Error, the ship doesn't exist!")
	elif value == 2:
		print("Error, the planet doesn't exist!")
	elif value == 3:
		print("Error, the ship name already used!")
	elif value == 4:
		print("Error, the planet name already used!")
	elif value == 5:
		print("Error, the ship is broken, You cannot move it!")
	elif value == 6:
		print("Error, the ship is not ready yet!")
	elif value == 7:
		print("Error, the ship is broken you cannot upgrade it!")
	elif value == 8:
		print("Error, there's no enough ressources!")
	elif value == 9:
		print("Error, the ship is not repairable because it's not broken!")
	elif value == 10:
		print("Error, the coordinates are not between 0 and 1000!")
	elif value == 11:
		print("Error, Aldebaran is not created yet!")


def reset():#Alessandro
	"""
	reset the game (prépare for a new game)
	"""
	gaming_tools.reset_game()
	print("The game has been reset!")
	return