# Variables
character_array = [
	"abcdefghijklmnopqrst",
	"uvwxyzABCDEFGHIJKLMN",
	"OPQRSTUVWXYZ01234567",
	"89.,!?+-=_`@#$%^&*()",
	"[];'\\/{}:\"|<>~	   "
]
special_buttons = "_x<^"

# Functions
def keyboard(title, max_characters = -1, default_text = "", cancel_output = ""):
	if max_characters == -1:
		max_characters = max_horizontal_characters

	cursor_pos = [0, 0]
	text = default_text
	special_button_selected = False
	special_button_index = 0

	while True:
		screen.fill(colors.get("background"))
		screen_text = "{}\n{}\n".format(wrap_text(title), pad_text(text))
		screen_text_height = text_height(screen_text) + new_line_offset

		screen.text(screen_text, color=colors.get("foreground"))

		for y, row in enumerate(character_array):
			for x, char in enumerate(row):
				color = colors.get("selection") if not special_button_selected and cursor_pos == [x, y] else colors.get("foreground")
				if special_button_selected and cursor_pos == [x, y]:
					color = colors.get("previous")
				screen.text(char, x * character_width, y * character_full_height + screen_text_height, color=color)

		for i, button in enumerate(special_buttons):
			color = colors.get("selection") if special_button_index == i else colors.get("foreground")
			if not special_button_selected and special_button_index == i:
				color = colors.get("previous")
			screen.text(button, i * character_width, text_bottom_position(button), color=color)

		screen.refresh()

		input = wait_input()

		if input == "a":
			if special_button_selected:
				if special_button_index == 0:
					if len(text) < max_characters:
						text += " "
				elif special_button_index == 1: return cancel_output
				elif special_button_index == 2: text = text[:-1]
				elif special_button_index == 3: return text
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