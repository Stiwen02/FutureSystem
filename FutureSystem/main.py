# import traceback

try:
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

		modules.append(filename)
		return module_class

	# Import
	from future import *
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
except Exception as error:
	from future import *
	
	screen_width = 160
	screen_height = 128

	character_width = 8
	character_height = 16

	new_line_offset = 2

	character_full_height = character_height + new_line_offset
	max_horizontal_characters = screen_width // character_width

	def wrap_text_d(text):
		words = text.split()
		new_lines = []
		line = ""

		for word in words:
			if len(line + word) + len(line.split()) <= max_horizontal_characters:
				line += ("" if line == "" else " ") + word
			else:
				new_lines.append(line)
				line = word
		new_lines.append(line)
		return "\n".join(new_lines)

	screen.text(wrap_text_d(repr(error)))
	# traceback.print_exc()
	while True:
		pass