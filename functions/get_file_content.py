import os
from google import genai
from google.genai import types
MAX_CHARS = 10000

#define get_file_content function. Takes working_directory and file_path string arguments, returns
#the contents of a file as a string
def get_file_content(working_directory, file_path):
	abs_working_dir = os.path.abspath(working_directory)
	file = os.path.abspath(os.path.join(working_directory, file_path))
	#test if file_path is outside of working_directory
	if not file.startswith(abs_working_dir):
		return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
	#test if file_path is a valid file
	if not os.path.isfile(file):
		return f'Error: File not found or is not a regular file: "{file_path}"'
	#read the file and return its content as a string
	try:
		with open(file, "r") as f:
			file_content = f.read(MAX_CHARS)
	except Exception as e:
		return f'Error opening the file: {e}'
	#test if file is longer than 10000 characters
	if os.path.getsize(file) > MAX_CHARS:
		return file_content + f'[...File "{file_path}" truncated at 10000 characters]'
	return file_content


#build the function declartion so that the LLM(gemini) knows what this function is
schema_get_file_content = types.FunctionDeclaration(
	name ="get_file_content",
	description="Reads the file specified in the file path.",
	parameters=types.Schema(
		type=types.Type.OBJECT,
		properties={
			"file_path": types.Schema(
				type=types.Type.STRING,
				description="The file path of the file to be read, relative to the working directory.",
			),
		},
	),
)