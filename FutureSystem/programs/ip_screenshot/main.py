# Import
from future import *
import modules.utils as utils
import modules.file_manager as file_manager
import random
import os

# Main
show_example = True
if show_example:
	screen.sync = 0

	screen.fill((0, 0, 0))
	screen.text("abcdefghijklmnopqrst\nuvwxyzABCDEFGHIJKLMN\nOPQRSTUVWXYZ12345678\n90!@#$%^&*()-=[]\\;',\n./_+{}|:\"<>?`~\nP P W W M M _ _\n\nP W M / \\ |\nP W M / \\ |\n\na o m i j q t\na o m i j q t")
	screen.refresh()

screenshot_start_x = 0
screenshot_start_y = 0
screenshot_end_x = 160 - 1
screenshot_end_y = 128 - 1

remind_around = 2.5

make_screenshot = True
if make_screenshot:
	file_name = utils.pad_text(str(random.randrange(0, 99999)), "0", "left", 5) + ".txt"
	
	print("\n\nScreenshotting to {}/screenshots/{}".format(os.getcwd(), file_name))
	screenshot = str(screenshot_end_x - screenshot_start_x + 1) + "\n" + str(screenshot_end_y - screenshot_start_y + 1) + "\n"
	
	if not file_manager.directory_exists("screenshots"):
		file_manager.create_directory("screenshots")
		print("'screenshots' directory not found but is now created")
	
	for x in range(screenshot_start_x, screenshot_end_x):
		for y in range(screenshot_start_y, screenshot_end_y):
			screenshot += "0" if screen._fb.pixel(x, y) == 0 else "1"
		if round(x % remind_around) == 0:
			print(str(round(x / screenshot_end_x * 100)) + "%: at X " + str(x) + " / " + str(screenshot_end_x) + "... (" + str(screenshot_start_x) + " to " + str(screenshot_end_x) + ")")

	print("Saving screenshot to " + os.getcwd() + "/screenshots/" + file_name)

	with open("screenshots/" + file_name, "w") as file:
		file.write(screenshot)

	print("Successfully saved screenshot to {}/screenshots/{}\n".format(os.getcwd(), file_name))