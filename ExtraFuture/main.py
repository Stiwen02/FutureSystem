# Import
from future import *
import modules.display_info as display_info
import modules.buttons as buttons

while True:
	try:
		screen.sync = 0
		
		display_info.notify("hi")
		
		while True:
			screen.fill((0, 0, 0))
			text = "Inputs:"
			
			text += "\n A: " + str(buttons.input_pressed("a")) + " (P3)"
			text += "\n B: " + str(buttons.input_pressed("b")) + " (P0)"
			text += "\n X: " + str(buttons.input_pressed("x")) + " (P1)"
			text += "\n Y: " + str(buttons.input_pressed("y")) + " (P8)"
			text += "\n UP: " + str(buttons.input_pressed("up")) + " (P9)"
			text += "\n DOWN: " + str(buttons.input_pressed("down")) + " (P2)"
			text += "\n LEFT: " + str(buttons.input_pressed("left")) + " (P13)"
			text += "\n RIGHT: " + str(buttons.input_pressed("right")) + " (P14)"
			text += "\n 1: " + str(buttons.input_pressed("1")) + " (P15)"
			text += "\n 2: " + str(buttons.input_pressed("2")) + " (P16)"
			text += "\n ls: " + str(buttons.input_pressed("ls")) + " (P5)"
			text += "\n rs: " + str(buttons.input_pressed("rs")) + " (P11)"
			
			screen.text(text)
			screen.refresh()
		
		from future import *
		import modules.file_manager as file_manager
		import modules.display_info as display_info
		import modules.user_input as user_input
		import modules.keyboard as keyboard

		categories = (
			"Python Programs",
			"Arcade Games",
			"Gameboy ROMs",
			"Mobile Apps",
			"Web Applications",
			"Desktop Applications",
			"Augmented Reality Games",
			"Virtual Reality Games",
			"Puzzle Games",
			"Adventure Games",
			"Sports Games",
			"Racing Games",
			"Simulation Games",
			"Educational Software",
			"Productivity Tools",
			"Audio Editing Software",
			"Video Editing Software",
			"Graphic Design Software",
			"3D Modeling Software",
			"Computer-Aided Design (CAD) Software",
			"Animation Software",
			"Data Analysis Tools",
			"Artificial Intelligence Software"
		)

		category = user_input.list(categories, "Choose category")
		answer = user_input.ask("Are you sure you want to enter {}?".format(category))
		display_info.notify("You said: " + ("Yes" if answer else "No"))

		display_info.notify("What's your name?")
		name = keyboard.keyboard("What's your name?")
		display_info.notify("Hello {}! How are you?".format(name))
		keyboard.keyboard("How are you?")
		display_info.notify("Nice!")
	except Exception as error:
		display_info.notify("{}\n\nType: {}".format(str(error), str(type(error).__name__)))