# Import
from future import *

# Variables
pins = {
	"a": MeowPin("P3", "IN"),
	"b": MeowPin("P0", "IN"),
	"x": MeowPin("P1", "IN"),
	"y": MeowPin("P9", "IN"),
	"up": MeowPin("P2", "IN"),
	"down": MeowPin("P13", "IN"),
	"left": MeowPin("P14", "IN"),
	"right": MeowPin("P15", "IN"),
	"options": MeowPin("P16", "IN"),
	"ls": MeowPin("P5", "IN"),
	"rs": MeowPin("P11", "IN")
}

# Don't use pin P8! It will make the SD card stop working until the board is restarted.
# my_pins = []
# my_pins.append(MeowPin("P8", "IN")); os.listdir()