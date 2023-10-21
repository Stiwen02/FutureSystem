# Import
from future import *
from modules.pins import *

# Main
screen.sync = 0

while True:
	output = ""

	for pin_name in pins.keys():
		pin = pins.get(pin_name)
		pin_number = pin.isPin
		pin_activated = False
		try:
			pin_activated = pin.getDigital() == 0
		except:
			pin_activated = False
		output += "{} ({}): {}\n".format(pin_name, pin_number, str(pin_activated))

	output += "A (sensor): {}\n".format(sensor.btnValue("a"))
	output += "B (sensor): {}\n".format(sensor.btnValue("b"))

	screen.fill((0, 0, 0))
	screen.text(output)
	screen.refresh()
