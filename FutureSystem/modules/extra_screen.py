# Import
from future import *
import sys

# Functions
def get_pixel_decimal(x, y):
	# Return RGB values
	return screen._fb.pixel(x, y)

def get_pixel_decimal(x, y):
	return screen._fb.pixel(x, y)

def show_builtin_message(message):
	return sys.modules.get("tinygui").showMessage(message)

def show_builtin_modal(message):
	return sys.modules.get("tinygui").showModal(message)