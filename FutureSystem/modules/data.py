# Import
import modules.file_manager as file_manager

# Variables
data_path = "data"

# Functions

# Start
if not file_manager.directory_exists(data_path):
	file_manager.create_directory(data_path)