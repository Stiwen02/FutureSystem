# Import
from modules.pins import *

# Functions
def input_pressed(input):
	try:
		if pins[input.lower()].getDigital():
			return False
		else:
			return True
	except:
		return False

def until_input(input, pressed = False):
	if not pressed:
		while input_pressed(input): pass
		while not input_pressed(input): pass
	while input_pressed(input): pass

def which_input_pressed(wait_until_released = True):
	for pin in pins.keys():
		if input_pressed(pin):
			if wait_until_released:
				until_input(pin, True)
			return pin
	return ""

def wait_input(wait_until_released = True):
	while True:
		which_input_pressed(wait_until_released)