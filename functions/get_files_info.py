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

#working_directory = "calculator"
#directory = "pkg"

#print(os.getcwd())

print(get_files_info("calculator", "."))












"""
#define get files function that will accept a directory path, and return a string that represents
#contents of that directory
def get_files_info(working_directory, directory=None):
	#create variable wd_contents to hold the list of elements in the working_directory
	wd_contents = os.listdir(working_directory)
	print(wd_contents)
	#check if directory is in wd_contents
	if directory in wd_contents:
		print("found")
		new_path = os.path.join(working_directory, directory)
		print(new_path)
		print(os.path.isdir(new_path))
		return "booyah"
	#else, directory is not in wd_contents. check every element in wd_contents to see if it is 
	#a sub-directory. check if directory is in each sub-directory 
	else:	
		for element in wd_contents:
			element_path = os.path.join(working_directory, element)
			if os.path.isdir(element_path):
				result = get_files_info(element_path, directory)
				return result
		return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"

#get_files_info("calculator", ".")
print(get_files_info("/home/yuh/workspace/github.com/crown-town-clown/ai-agent", "bin"))
#print(os.getcwd())
#print(os.path.abspath("/ai-agent"))
#print(os.path.isdir("functions"))

#google how to recursively search for a directory


















import os

define get_files_info function, accepts a directory path and returns a string that represents
the contents of that directory. It takes working_directory and directory as string arguments. 
If directory is outside working directory, return an error message

def get_files_info(working_directory, directory=None):
	#create variable wd_contents to hold a list of the working directory's contents
	wd_contents = os.listdir(working_directory)
	print(wd_contents)
	#test if directory is in the working directory
	if directory in wd_contents or directory == working_directory:
		#test if the directory is a directory
		if not os.path.isdir(directory):
			return f"Error: '{directory}' is not a directory"
		else:
			#build and return a string representing the contents of the directory
			print("yo")
	#else, directory is not in the working directory's elements
	#check each element in the working directory to see if it is a sub-directory
	else:
		for element in wd_contents:
			#if an element is a sub-directory, recursively cally get_files_info to check if the 
			#directory is inside of it
			if os.path.isdir(element):
				sub_dir = 

		return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"

#test get_files_info
print(get_files_info("/home/yuh/workspace", "/home/yuh/workspace/github.com/crown-town-clown/ai-agent/functions"))
print(os.getcwd())
print(os.path.abspath("/ai-agent"))
"""

#6/26, 2056, i've spent the last 20-30 mins coming to the realization that i will need to use recursion
#with this function, i think? check if the directory is in the working directory's contents. But,
#what that means is that I will have to check if there are any other directories in the contents 
#as well and then call the function on them to test if directory we are looking for is there

#focus on testing if the directory is in the working first, which means testing sub-directories
#of the working directory as well. if after going through the sub-dirs the directory isn't found
#then return that it is outside the working directory. if it is found, but not a directory(ie, a 
#file), then return that it is not a directory