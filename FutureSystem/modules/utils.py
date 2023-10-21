# Import
from future import *
import modules.future_info as future_info

# Functions
def to_matrix(list, row_length):
	return [list[i:i + row_length] for i in range(0, len(list), row_length)]

def wrap_text(text):
	words = text.split()
	new_lines = []
	line = ""

	for word in words:
		if len(line + word) + len(line.split()) <= future_info.max_horizontal_characters:
			line += ("" if line == "" else " ") + word
		else:
			new_lines.append(line)
			line = word
	new_lines.append(line)
	return "\n".join(new_lines)

def pad_text(string, padding = "_", side = "right", max_length = -1):
	if max_length == -1: max_length = future_info.max_horizontal_characters
	num_paddings = max_length - len(string)
	
	if side == "left":
		return padding * num_paddings + string
	elif side == "right":
		return string + padding * num_paddings
	return string

def censor_text(text, show = 3, side = "right"):
	if show <= 0:
		return "*" * len(text)

	if side == "left":
		return "*" * (len(text) - show) + text[-show:]
	elif side == "right":
		return text[:show] + "*" * (len(text) - show)
	return string

def text_size(text, new_line_offset = -1):
	return (text_width(text), text_height(text, new_line_offset))

def text_width(text):
	return max(len(line) for line in text.split("\n")) * character_width

def text_height(text, new_line_offset = -1):
	new_line_offset = new_line_offset if new_line_offset != -1 else future_info.new_line_offset
	return (text.count("\n") + 1) * (future_info.character_height + new_line_offset)

def text_bottom_position(text, space = 0):
	total_height_px = text_height(text) + (space * future_info.character_full_height)
	return future_info.screen_height - total_height_px