# Import
from future import *
import modules.future_info as future_info

# Functions
def input_pressed(input):
	if future_info.pins[input.lower()].getDigital():
		return False
	else:
		return True

def until_input(input, pressed = False):
	if not pressed:
		while input_pressed(input): pass
		while not input_pressed(input): pass
	while input_pressed(input): pass

def wait_input(wait_stop = True):
	while True:
		for pin in future_info.pins.keys():
			if input_pressed(pin):
				if wait_stop:
					until_input(pin, True)
				return pin