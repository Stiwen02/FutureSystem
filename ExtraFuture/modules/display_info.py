# Import
from future import *
import modules.utils as utils
import modules.future_info as future_info
import modules.buttons as buttons

# Functions
def notify(message, wrap = True, button = "a"):
	screen.fill(future_info.colors.get("background"))
	screen.text(utils.wrap_text(message) if wrap else message, color=future_info.colors.get("foreground"))
	screen.text("Press {} to continue".format(button.upper()), 0, utils.text_bottom_position(message), color=future_info.colors.get("foreground"))
	screen.refresh()
	
	buttons.until_input(button.lower())
	
	screen.fill(future_info.colors.get("background"))
	screen.refresh()