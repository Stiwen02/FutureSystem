# Import
from future import *
import modules.utils as utils
import modules.file_manager as file_manager
import random
import os

# Main
screenshot_start_x = 0
screenshot_start_y = 0
screenshot_width = 8
screenshot_height = 8

remind_around = 2.5

def make_screenshot(file_name = ""):
	if file_name == "":
		file_name = utils.pad_text(str(random.randrange(0, 99999)), "0", "left", 5) + ".txt"
	else:
		if len(file_name) == 1:
			if file_name.isupper():
				file_name = "upper_" + file_name
			elif file_name.islower():
				file_name = "lower_" + file_name
		file_name += ".txt"

	print("\n\nScreenshotting to {}/screenshots/{}".format(os.getcwd(), file_name))
	screenshot = str(screenshot_width) + "\n" + str(screenshot_height) + "\n"

	if not file_manager.directory_exists("screenshots"):
		file_manager.create_directory("screenshots")
		print("'screenshots' directory not found but is now created")

	screenshot_end_x = screenshot_start_x + (screenshot_width - 1)
	screenshot_end_y = screenshot_start_y + (screenshot_height - 1)

	for x in range(screenshot_start_x, screenshot_end_x):
		for y in range(screenshot_start_y, screenshot_end_y):
			screenshot += "0" if screen._fb.pixel(x, y) == 0 else "1"
		if round(x % remind_around) == 0:
			print(str(round(x / screenshot_end_x * 100)) + "%: at X " + str(x) + " / " + str(screenshot_end_x) + "... (" + str(screenshot_start_x) + " to " + str(screenshot_end_x) + ")")

	print("Saving screenshot to " + os.getcwd() + "/screenshots/" + file_name)

	with open("screenshots/" + file_name, "w") as file:
		file.write(screenshot)

	print("Successfully saved screenshot to {}/screenshots/{}\n".format(os.getcwd(), file_name))

if file_manager.directory_exists("screenshots"):
	for file in os.listdir("screenshots"):
		os.remove("screenshots/" + file)

unallowed_characters = {
	"\\": "back slash",
	"<": "less than",
	">": "greater than",
	":": "colon",
	"\"": "double quote",
	"/": "forward slash",
	"|": "vertical bar or pipe",
	"?": "question mark",
	"*": "asterisk",
	".": "comma"
}

screen.sync = 0
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=[]\\;',./_+{}|:\"<>?`~"
characters = "?"
for character in characters:
	file_name_to_use = character
	if any(ext in file_name_to_use for ext in unallowed_characters.keys()):
		file_name_to_use = unallowed_characters.get(file_name_to_use)
	screen.fill((0, 0, 0))
	screen.text(character, 0, 0)
	screen.refresh()
	make_screenshot(file_name_to_use)