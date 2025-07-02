import os
import subprocess

#define run_python_file function to run python files. takes working_directory and file_path string
#arguments
def run_python_file(working_directory, file_path):
	#create abs_working_dir variable to hold working_directory path
	abs_working_dir = os.path.abspath(working_directory)
	#create file variable to hold file_path path
	file = os.path.abspath(os.path.join(working_directory, file_path))
	#test if file_path is outside working_directory
	if not file.startswith(abs_working_dir):
		return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
	#test if file_path exists
	if not os.path.exists(file):
		return f'Error: File "{file_path}" not found'
	#test if file_path ends in ".py"
	if file_path[-3:] != ".py":
		return f'Error: "{file_path}" is not a Python file'
	#use subprocess.run function to execute the python file
	#create output variable to hold the result of executing the file
	try:
		file_output = subprocess.run(["python3", file], capture_output=True, cwd=abs_working_dir, timeout=30, text=True)
		#create list variable result to hold the parts of file_output we need
		result = []
		if file_output.stdout:
			result.append(f'STDOUT: {file_output.stdout}')
		if file_output.stderr:
			result.append(f'STDERR: {file_output.stderr}')
		if file_output.returncode != 0:
			result.append(f'Process exited with code "{file_output.returncode}')
		if not file_output.stdout and not file_output.stderr:
			return "No output produced."
		return "\n".join(result)
	except Exception as e:
		return f'Error executing Python file: {e}'