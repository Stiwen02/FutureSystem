# Import
import math

# Variables
screen_width = 160
screen_height = 128

character_width = 8
character_height = 8

new_line_offset = 2

character_full_height = character_height + new_line_offset
max_horizontal_characters = math.floor(screen_width // character_width)

colors = {
	"background": (0, 0, 0),
	"foreground": (255, 255, 255),
	"selection": (255, 0, 0),
	"previous": (0, 0, 255),
	"next": (0, 255, 0)
}