# Functions
def is_file(path):
	try:
		with open(path, "r") as file:
			return True
	except:
		return False

def copy_file(source, destination):
	with open(source, "r") as source_file:
		with open(destination, "w") as destination_file:
			destination_file.write(source_file.read())

def copy_cfg(cfg_path = "/cfg", sd_path = "/sd"):
	if "cfg" in os.listdir(sd_path):
		print("Clearing CFG files on SD")
		for file in os.listdir(sd_path + "/cfg"):
			path = sd_path + "/cfg/"+  file
			if is_file(path):
				print(" Removing SD CFG file " + path)
				os.remove(path)
			else:
				print(" SD CFG directory found but not removed: " + path)
	print("Copying CFG files at " + cfg_path + " to SD " + sd_path + "/cfg")
	if not "cfg" in os.listdir(sd_path):
		os.mkdir(sd_path + "/cfg")
	for file in os.listdir(cfg_path):
		path = cfg_path + "/" + file
		dest = sd_path + "/cfg/" + file
		if is_file(path):
			print(" Copying CFG file " + path + " to SD " + dest)
			copy_file(path, dest)
		else:
			print(" CFG directory found but not copied to SD: " + path)
	print("Done\n")

def copy_sd_cfg(cfg_path = "/cfg", sd_path = "/sd"):
	print("Copying SD's CFG files at" + sd_path + "/cfg to CFG" + cfg_path)
	for file in os.listdir(sd_path + "/cfg"):
		path = sd_path + "/cfg/" + file
		dest = cfg_path + "/" + file
		if is_file(path):
			print(" Copying SD's CFG file " + path + " to CFG " + dest)
			copy_file(path, dest)
		else:
			print(" SD's CFG directory found but not copied to CFG: " + path)
	print("Done\n")

# screen to choose if to copy CFG to SD or copy SD's CFG to CFG