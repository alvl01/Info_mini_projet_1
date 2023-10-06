import gaming_tools
import time.time
import random.randint

## info
def help_game():#jugurtha
	"""
	explain how to use the other functions
	"""
	print("ship_state affiche ...")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	return

def ship_state(ship):#anderson
	"""
	diplay information about the ship

	parameters
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
	print("")
	return

def planet_position(planet):#ammar
	"""
	display planet position

	parameters
	----------
	planet: name of the planet (str)
	"""
	if not gaming_tools.planet_exists(ship):
		error(2)
		return
	return

def planet_resources(planet):#abdelaziz
	"""
	display the quantity of ressources of a planet

	parameters
	----------
	planet: name of the planet (str)
	"""
	if not gaming_tools.planet_exists(ship):
		error(2)
		return
	return

## Action
def move(ship):#Alessandro
	"""
	move the ship

	parameters
	----------
	ship: name of the ship (str)
	"""
	if not gaming_tools.ship_exists(ship):
		error(1)
		return

	return

def upgrade(ship):#abdelaziz
	"""
	uprade the ship
	
	parameters
	----------
	ship: name of the ship (str)
	"""
	if not gaming_tools.ship_exists(ship):
		error(1)
		return
	return

def repare(ship):#jugurtha
	"""
	repare the ship

	parameters
	----------
	ship: name of the ship (str)
	"""
	if not gaming_tools.ship_exists(ship):
		error(1)
		return
	return

def create_planet(name):#anderson
	"""
	create a planet
	display a confirmation

	parameters
	----------
	name: name of the planet
	"""
	if not gaming_tools.planet_exists(ship):
		error(4)
		return
	return

def create_ship(name):#ammar
	"""
	create a ship
	display a confirmation

	parameters
	----------
	name: name of the ship
	"""
	if gaming_tools.ship_exists(ship):
		error(3)
		return
	return

def error(value):#Alessandro
	if value == 1:
		print("error the ship doesn't exist")
	elif value == 2:
		print("error the planet doesn't exist")
	elif value == 3:
		print("ship name already used")
	elif value == 4:
		print("planet name already used")
	return


def reset():#Alessandro
	"""
	reset the game (prépare for a new game)
	"""
	return