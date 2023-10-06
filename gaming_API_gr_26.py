import gaming_tools
import time.time
import random.randint

## info
def help_game():#jugurtha
	print("ship_state affiche ...")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")

def ship_state(ship):#anderson
	loc = gaming_tools.get_ship_location(ship)
	speed = gaming_tools.get_ship_speed(ship)
	broken = gaming_tools.is_ship_broken(ship)
	ready = gaming_tools.get_when_ship_is_ready(ship)
	print("")

def planet_position():#ammar
	pass

def planet_resources():#abdelaziz
	pass

## Action
def move():#Alessandro
	pass

def upgrade():#abdelaziz
	pass

def repare():#jugurtha
	pass

def create_planet():#anderson
	pass

def create_ship():#ammar
	pass


def reset():#Alessandro
	pass