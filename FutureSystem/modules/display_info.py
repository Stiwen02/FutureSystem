# Import
from future import *

# Functions
def notify(message, wrap = True, button = "a"):
	screen.fill(info.colors.get("background"))
	screen.text(wrap_text(message) if wrap else message, color=info.colors.get("foreground"))
	screen.text("Press {} to continue".format(button.upper()), 0, text_bottom_position(message), color=info.colors.get("foreground"))
	screen.refresh()

	buttons.until_input(button.lower())

	screen.fill(info.colors.get("background"))
	screen.refresh()