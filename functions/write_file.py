import os
from google import genai
from google.genai import types

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


#build the declaration for write_file so that the LLM(gemini) knows how it works
schema_write_file = types.FunctionDeclaration(
	name="write_file",
	description="Writes or overwrites a Python file in the specified file path with the content provided.",
	parameters=types.Schema(
		type=types.Type.OBJECT,
		properties={
			"file_path": types.Schema(
				type=types.Type.STRING,
				description="The file path of the specified file, relative to the working directory.",
			),
			"content": types.Schema(
				type=types.Type.STRING,
				description="The content that will be written to the file.",
			),
		},
	),
)