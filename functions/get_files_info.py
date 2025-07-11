#6/27, 1755, starting over
import os
from google import genai
from google.genai import types

#define get files function that will accept a directory path, and return a string that represents
#contents of that directory
def get_files_info(working_directory, directory=None):
	abs_working_dir = os.path.abspath(working_directory)
	target_dir = abs_working_dir
	#test if directory is valid or outside working_directory
	if directory:
		target_dir = os.path.abspath(os.path.join(working_directory, directory))
	if not target_dir.startswith(abs_working_dir):
		return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
	if not os.path.isdir(target_dir):
		return f'Error: "{directory}" is not a directory'
	#build and return a string representing the contents of the directory
	dir_contents = []
	#add each file's name, size in bytes, and whether it's a directory or not to the string
	try:
		for element in os.listdir(target_dir):
			element_path = os.path.join(target_dir, element)
			size = os.path.getsize(element_path)
			is_dir = os.path.isdir(element_path)
			file_content = f"- {element}: file_size={size} bytes, is_dir={is_dir}"
			dir_contents.append(file_content)
	except Exception as e:
		return f'Error list files: {e}'
	return "\n".join(dir_contents)


#build the declaration for get_files_info to tell the LLM(gemini), how to use it
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)