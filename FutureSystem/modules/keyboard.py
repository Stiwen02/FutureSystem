# Import
from future import *
import time
import modules.future_info as future_info
import modules.buttons as buttons
import modules.utils as utils
import modules.user_input as user_input

# Variables
character_array = [
	"abcdefghijklmnopqrst",
	"uvwxyzABCDEFGHIJKLMN",
	"OPQRSTUVWXYZ01234567",
	"89.,!?+-=_`@#$%^&*()",
	"[];'\\/{}:\"|<>~      "
]
special_characters = {
	".": "Period",
	",": "Comma",
	"!": "Exclamation",
	"?": "Question",
	"+": "Plus",
	"-": "Minus",
	"=": "Equals",
	"_": "Underscore",
	"`": "Backtick",
	"@": "At",
	"#": "Hashtag",
	"$": "Dollar Sign",
	"%": "Percentage",
	"^": "Caret",
	"&": "And",
	"*": "Asterisk",
	"(": "Parentheses",
	")": "Parentheses",
	"[": "Brackets",
	"]": "Brackets",
	";": "Semicolon",
	"'": "Quote",
	"\\": "Backslash",
	"/": "Slash",
	"{": "Braces",
	"}": "Braces",
	":": "Colon",
	"\"": "Quotation",
	"|": "Pipe",
	"<": "Less than",
	">": "More than",
	"~": "Tilde",
	" ": "Spacebar"
}
special_buttons = "_x<^"

# Functions
def keyboard(title, max_characters = -1, default_text = "", cancel_output = ""):
	if max_characters == -1:
		max_characters = future_info.max_horizontal_characters

	cursor_pos = [0, 0]
	text = default_text
	special_button_selected = False
	special_button_index = 0

	while True:
		screen.fill(future_info.colors.get("background"))
		screen_text = "{}\n{}\n".format(utils.wrap_text(title), utils.pad_text(text + ("|" if (time.ticks_ms() % 1000) < 500 else " ")))
		screen_text_height = utils.text_height(screen_text) + future_info.new_line_offset

		screen.text(screen_text, color=future_info.colors.get("foreground"))

		for y, row in enumerate(character_array):
			for x, char in enumerate(row):
				color = future_info.colors.get("selection") if not special_button_selected and cursor_pos == [x, y] else future_info.colors.get("foreground")
				if special_button_selected and cursor_pos == [x, y]:
					color = future_info.colors.get("previous")
				screen.text(char, x * future_info.character_width, y * future_info.character_full_height + screen_text_height, color=color)

		for i, button in enumerate(special_buttons):
			color = future_info.colors.get("selection") if special_button_index == i else future_info.colors.get("foreground")
			if not special_button_selected and special_button_index == i:
				color = future_info.colors.get("previous")
			screen.text(button, i * future_info.character_width, utils.text_bottom_position(button), color=color)
		
		if special_button_selected:
			if special_button_index == 0: description = "Spacebar"
			elif special_button_index == 1: description = "Cancel"
			elif special_button_index == 2: description = "Backspace"
			elif special_button_index == 3: description = "Done"
		else:
			letter = character_array[cursor_pos[1]][cursor_pos[0]]
			description = letter
			if letter.isupper():
				description = "Uppercase " + description
			elif letter.islower():
				description = "Lowercase " + description
			if description in special_characters.keys():
				description = special_characters.get(description)
			if len(description) > 1:
				description += " ({})".format(letter)
		screen.text(description, future_info.screen_width - utils.text_width(description), future_info.screen_height - utils.text_height(description, 0))
		if special_button_selected:
			position_text = "X:{}".format(str(special_button_index + 1))
		else:
			position_text = "X:{},Y:{}".format(str(cursor_pos[0] + 1), str(cursor_pos[1] + 1))
		screen.text(position_text, future_info.screen_width - utils.text_width(position_text), future_info.screen_height - utils.text_height(position_text + "\n"))
		
		screen.refresh()
		input = buttons.which_input_pressed()

		if input == "a":
			if special_button_selected:
				if special_button_index == 0:
					if len(text) < max_characters:
						text += " "
				elif special_button_index == 1:
					if user_input.ask(("Are you sure you want to cancel and proceed with\n" + cancel_output) if not cancel_output == "" else "Are you sure you want to cancel?"):
						return cancel_output
				elif special_button_index == 2: text = text[:-1]
				elif special_button_index == 3:
					if user_input.ask("Are you sure you are done with\n" + text):
						return text
			else:
				if len(text) < max_characters:
					text += character_array[cursor_pos[1]][cursor_pos[0]]
		elif input == "b":
			special_button_selected = not special_button_selected

		if input == "up":
			if not special_button_selected:
				cursor_pos[1] -= 1
		elif input == "down":
			if not special_button_selected:
				cursor_pos[1] += 1

		elif input == "left":
			if special_button_selected:
				special_button_index -= 1
			else:
				cursor_pos[0] -= 1
		elif input == "right":
			if special_button_selected:
				special_button_index += 1
			else:
				cursor_pos[0] += 1

		cursor_pos[0] %= len(character_array[0])
		cursor_pos[1] %= len(character_array)

		special_button_index %= len(special_buttons)