#6/27, 1755, starting over
import os

#define get files function that will accept a directory path, and return a string that represents
#contents of that directory
def get_files_info(working_directory, directory=None):
	os.chdir("/home/yuh/workspace/github.com/crown-town-clown/ai-agent")
	for root, dirs, files in os.walk(os.getcwd()):
		if working_directory in root and directory == ".":
			#build and return a string representing the contents of the directory
			dir_contents = f"Result for current directory:\n"
			#add each file's name, size in bytes, and whether it's a directory or not to the string
			for element in os.listdir(root):
				element_path = os.path.join(root, element)
				element_contents = f"- {element}: file_size={os.path.getsize(element_path)} bytes, is_dir={os.path.isdir(element_path)}\n"
				dir_contents += element_contents 
			return dir_contents
		if working_directory in root and directory in dirs:
			#build and return a string representing the contents of the directory
			dir_contents = f"Result for '{directory}' directory:\n"
			dir_path = os.path.join(root, directory)
			#add each file's name, size in bytes, and whether it's a directory or not to the string
			for element in os.listdir(dir_path):
				element_path = os.path.join(dir_path, element)
				element_contents = f"- {element}: file_size={os.path.getsize(element_path)} bytes, is_dir={os.path.isdir(element_path)}\n"
				dir_contents += element_contents
			return dir_contents
		elif working_directory in root and directory not in dirs:
			if directory in files:
				return f"Error: '{directory}' is not a directory"
			else:
				return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"


#print(get_files_info("calculator", "."))
