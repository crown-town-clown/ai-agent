import os

#define write_file function to write and overwrite files
def write_file(working_directory, file_path, content):
	#create variable abs_working_path to hold working_directory path 
	abs_working_path = os.path.abspath(working_directory)
	#create file variable to hold file_path absolute path
	file = os.path.abspath(os.path.join(working_directory, file_path))
	#test if file_path is outside working_directory
	if not file.startswith(abs_working_path):
		return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
	#if the file doesn't exist, create it. if there are any errors, return an error string
	if not os.path.exists(file):
		try:
			os.makedirs(os.path.dirname(file), exist_ok=True)
		except Exception as e:
			return f'Error creating file: {e}'
	#overwrite the contents of the file with content
	if os.path.exists(file) and os.path.isdir(file):
		return f'Error: "{file_path}" is a directory, not a file'
	try:
		with open(file, "w") as f:
			f.write(content)
		#if successful, return a string with success message
		return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
	except Exception as e:
		return f'Error writing to the file: {e}'