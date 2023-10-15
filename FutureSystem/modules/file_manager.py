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

def file_exists(path):
	return os.path.isfile(path)

def delete_file(path):
	os.remove(path)

def create_directory(path):
	os.mkdir(path)

def rename_directory(source_path, dest_path):
	os.rename(source_path, dest_path)

def move_directory(source_path, dest_path):
	os.rename(source_path, dest_path)

def directory_exists(path):
	return os.path.isdir(path)

def delete_directory(path):
	os.rmdir(path)

def delete_full_directory(path):
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
	result = tuple(file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)))
	return result if return_tuple else list(result)

def list_directories(path = ".", return_tuple=False):
	result = tuple(directory for directory in os.listdir(path) if os.path.isdir(os.path.join(path, directory)))
	return result if return_tuple else list(result)

def is_file(path):
	return os.path.isfile(path)

def is_directory(path):
	return os.path.isdir(path)

def cd(path):
	os.chdir(path)

def current_path():
	os.getcwd()

def absolute_path(path):
	os.path.abspath(path)