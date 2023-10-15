# Functions
def list(items, title, selected=0, space=-1, wrap=True, cancel=False, bottom_space=False):
	if bottom_space and space == -1:
		space = 0

	current_index = selected
	current_page = 0

	pages = []
	for i, item in enumerate(items):
		if i % 8 == 0:
			pages.append([])
		pages[len(pages) - 1].append(item)

	while True:
		screen.fill(info.colors.get("background"))
		title_text = wrap_text(title) if wrap else title
		title_height = text_height(title_text + "\n") + new_line_offset

		screen.text(title_text, color=info.colors.get("foreground"))

		if len(pages) > 1:
			page_text = "\nPage: {}/{}".format(current_page + 1, len(pages))
			screen.text(page_text, 0, text_bottom_position(page_text), color=info.colors.get("foreground"))

		for i, item in enumerate(pages[current_page]):
			color = info.colors.get("selection") if i == current_index else info.colors.get("foreground")
			y = 0

			if bottom_space:
				y = text_bottom_position(item, len(pages[current_page]) - 1 - i)
			else:
				y = title_height + (i + (1 if i >= space else 0)) * info.character_full_height

			screen.text(item, 0, y, color=color)

		screen.refresh()

		input = buttons.wait_input()

		if input == "a":
			return pages[current_page][current_index]
		elif input == "b" and cancel:
			return ""

		if input == "up":
			current_index -= 1
		elif input == "down":
			current_index += 1
		elif input == "left" and len(pages) > 1:
			current_page -= 1
			current_index = 0
		elif input == "right" and len(pages) > 1:
			current_page += 1
			current_index = 0

		current_page %= len(pages)
		current_index %= len(pages[current_page])