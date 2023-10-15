from future import *
try:
	import modules.keyboard as keyboard
	import modules.display_info as display_info

	name = keyboard.keyboard("What's your name?")
	display_info.notify("Hello, " + name + ".")
except Exception as error:
	screen.text(repr(error))