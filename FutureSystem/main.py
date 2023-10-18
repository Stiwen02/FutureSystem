# import traceback
from future import *
import gc

# Import functionality
modules = []

def import_module(name, to_globals=False):
	global modules

	name = name
	filename = "modules/" + name + ".py"

	if filename in modules:
		raise Exception("Module '" + filename + "' already imported")

	with open(filename, "r") as file:
		code = file.read()
	bytecodes = compile(code, filename, "exec")

	exec_locals = {}
	exec(bytecodes, exec_locals)
	
	if to_globals:
		exec(bytecodes, globals())

	module_class = type(name, (), exec_locals)
	del exec_locals
	del name
	del code
	del bytecodes
	gc.mem_free()
	gc.mem_alloc()

	modules.append(filename)
	del filename
	return module_class

# Import
import_module("keyboard", True)
import_module("file_manager", True)
import_module("list", True)
import_module("utils", True)
import_module("info", True)
import_module("display_info", True)
import_module("buttons", True)
import_module("user_input", True)
import_module("screen", True)
import_module("bitmap", True)
import_module("bluetooth", True)
import_module("buzzer", True)
import_module("data", True)
import_module("execute", True)
import_module("game_engine", True)
import_module("text", True)
import_module("wifi", True)

# Main
screen.sync = 0

name = keyboard("What's your name?")
notify("Hello, " + name + ".")