# Import
import modules.list as list

# Functions
def ask(message, option_yes = "Yes", option_no = "No", selected = 1, wrap = True, cancel = False):
	return list.list(items = [option_yes, option_no], title = message, selected = selected, wrap = wrap, cancel = cancel, bottom_space = True) == option_yes