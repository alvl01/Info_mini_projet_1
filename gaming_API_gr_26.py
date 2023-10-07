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
# planet ressource et planet postion on ete combiné
def planet_state(planet):#ammar#abdelaziz
	"""
	display information about the planet

	parameters
	----------
	planet: name of the planet (str)
	"""
	if not gaming_tools.planet_exists(ship):
		error(2)
		return
	return

## Action
def get_distance(ship, planet):
	if not gaming_tools.ship_exists(ship):
		error(1)
		return
	if not gaming_tools.planet_exists(ship):
		error(2)
		return
	ship_x, ship_y = gaming_tools.get_ship_location(ship)
	planet_x, planet_y = gaming_tools.get_planet_location(planet)
	return ((ship_x - planet_x) ** 2 + (ship_y - planet_y) ** 2) ** (1/2)

def text_time(time):
	return (time // 60 == 0 ? "" : str(time // 60) + "min ") + str(time % 60) + "s"



def move(ship, planet):#Alessandro
	"""
	move the ship

	parameters
	----------
	ship: name of the ship (str)
	"""
	if not gaming_tools.ship_exists(ship):
		error(1)
		return
	if not gaming_tools.planet_exists(ship):
		error(2)
		return
	if gaming_tools.is_ship_broken(ship):
		error(5)
		return
	if gaming_tools.get_when_ship_is_ready(ship) != 0:
		errror(6)
		return
	# change position of the ship
	ship_speed = gaming_tools.get_ship_speed(ship)
	distance = get_distance(ship, planet)
	time = distance / ship_speed
	gaming_tools.set_ship_location(ship, planet)
	# is the ship broken
	if not random.randint(0, 2):
		gaming_tools.set_ship_broken(ship, True)
	# display the time
	print("you will land in", text_time(int(time)))
	# set waiting time
	gaming_tools.set_when_ship_is_ready(ship, time)
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
	if gaming_tools.planet_exists(ship):
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

def error(value):
	if value == 1:
		print("error the ship doesn't exist!")
	elif value == 2:
		print("error the planet doesn't exist!")
	elif value == 3:
		print("ship name already used!")
	elif value == 4:
		print("planet name already used!")
	elif value == 5:
		print("the ship is broken you can not move it!")
	elif value == 6:
		print("the ship is not ready yet!")
	return


def reset():#Alessandro
	"""
	reset the game (prépare for a new game)
	"""
	return