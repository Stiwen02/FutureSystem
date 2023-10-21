# Import
from future import *
from modules.keyboard import *
import modules.display_info as display_info

# Main
screen.sync = 0
name = keyboard("What's your name?")
display_info.notify("Hello, " + name + ".")