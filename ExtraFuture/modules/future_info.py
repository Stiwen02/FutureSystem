# Import
from future import *

# Variables
screen_width = 160
screen_height = 128

character_width = 8
character_height = 16

new_line_offset = 2

character_full_height = character_height + new_line_offset
max_horizontal_characters = screen_width // character_width

pins = {
	"a": MeowPin("P3", "IN"),
	"b": MeowPin("P0", "IN"),
	"x": MeowPin("P1", "IN"),
	"y": MeowPin("P8", "IN"),
	"up": MeowPin("P9", "IN"),
	"down": MeowPin("P2", "IN"),
	"left": MeowPin("P13", "IN"),
	"right": MeowPin("P14", "IN"),
	"1": MeowPin("P15", "IN"),
	"2": MeowPin("P16", "IN"),
	"ls": MeowPin("P5", "IN"),
	"rs": MeowPin("P11", "IN")
}

colors = {
	"background": (0, 0, 0),
	"foreground": (255, 255, 255),
	"selection": (255, 0, 0),
	"prediction": (0, 0, 255),
	"previous": (0, 255, 0)
}