# Import
import os

# Functions
def write_file(path, content):
	with open(path, "w") as file:
		file.write(content)

def read_file(path):
	with open(path, "r") as file:
		return file.read()

def rename_file(source_path, dest_path):
	os.rename(source_path, dest_path)

def move_file(source_path, dest_path):
	os.rename(source_path, dest_path)

def clone_file(source_path, dest_path):
	write_file(dest_path, read_file(source_path))

def file_exists(path):
	try:
		read_file(path)
		return True
	except:
		return False

def delete_file(path):
	os.remove(path)

def create_directory(path):
	os.mkdir(path)

def rename_directory(source_path, dest_path):
	os.rename(source_path, dest_path)

def move_directory(source_path, dest_path):
	os.rename(source_path, dest_path)

def directory_exists(path):
	current_cwd = "/"
	try:
		current_cwd = os.getcwd()
	except:
		current_cwd = "/"
	try:
		os.chdir(path)
		os.chdir(current_cwd)
		return True
	except:
		try:
			os.chdir(current_cwd)
			return False
		except:
			return False
	return False

def delete_directory(path):
	os.rmdir(path)

def delete_entire_directory(path):
	# finish (os.walk doesn't exist, finish and use walk(path))
	for root, dirs, files in os.walk(path, topdown=False):
		for file in files:
			file_path = os.path.join(root, file)
			os.remove(file_path)
		for dir in dirs:
			dir_path = os.path.join(root, dir)
			os.rmdir(dir_path)
	os.rmdir(path)

def list_all(path = ".", return_tuple=False):
	return tuple(os.listdir()) if return_tuple else os.listdir()

def list_files(path = ".", return_tuple=False):
	result = tuple(file for file in os.listdir(path) if is_file(join_paths(path, file)))
	return result if return_tuple else list(result)

def list_directories(path = ".", return_tuple=False):
	result = tuple(directory for directory in os.listdir(path) if is_directory(join_paths(path, directory)))
	return result if return_tuple else list(result)

def walk(path):
	# finish
	return []

def join_paths(path, *paths):
	# finish (with support for relative paths)
	return ""

def is_file(path):
	return file_exists(path) and not directory_exists(path)

def is_directory(path):
	return directory_exists(path) and not file_exists(path)

def parent_directory(path):
	return "/".join(path.replace("\\", "/").split("/")[:-1])

def file_name(path):
	return path.replace("\\", "/").split("/")[-1]

def directory_name(path):
	return path.replace("\\", "/").split("/")[-1]

def cd(path):
	os.chdir(path)

def current_path():
	return os.getcwd()

def absolute_path(path):
	# finish (relative paths don't work)
	return join_paths(current_path(), path)