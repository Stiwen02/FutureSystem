# Import
import sys
import os

# Functions
def write_file(path, content):
    with open(path, "w") as file:
        file.write(content)

def read_file(path):
    with open(path) as file:
        return file.read()

def rename_file(path, new_path):
    os.rename(path, new_path)

def file_exists(path):
    return os.path.isfile(path)

def delete_file(path):
    os.remove(path)

def create_directory(path):
    os.mkdir(path)

def rename_directory(path, new_path):
    os.rename(path, new_path)

def directory_exists(path):
    return os.path.isdir(path)

def delete_directory(path):
    os.rmdir(path)

def list_files(path):
    return tuple(file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)))

def list_directories(path):
    return tuple(directory for directory in os.listdir(path) if os.path.isdir(os.path.join(path, directory)))