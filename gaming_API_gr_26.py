import gaming_tools
def launch():
	print("pour jouer ...")
## info
def help_game():
	print("ship_state affiche ...")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")

def ship_state(ship):
	gaming_tools.get_ship_location(ship)
	gaming_tools.get_ship_speed(ship)
	gaming_tools.is_ship_broken(ship)
	gaming_tools.get_when_ship_is_ready(ship)

def planet_position():
	pass
def get_time():
	pass
def planet_resources():
	pass

## Action
def move():
	pass

def upgrade():
	pass

def repare():
	pass