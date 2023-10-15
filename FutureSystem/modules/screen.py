# Import
from future import *

# Functions
def get_pixel(x, y):
	# Return RGB values
	return screen._fb.pixel(x, y)