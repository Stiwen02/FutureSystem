# Import
import sys
import os

# Functions
def format_exception(exc, delete_file=True):
	exception_path = "exception.txt"
	with open(exception_path, "w") as file:
		sys.print_exception(exc, file)
		exception = file.read()
	if delete_file:
		os.remove(exception_path)
	return exception

def format_exc(exc, delete_file=True):
	return format_exception(exc, delete_file)