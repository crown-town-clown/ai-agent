import os
from google import genai
from google.genai import types
from functions.get_files_info import get_files_info, schema_get_files_info 
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.run_python import run_python_file, schema_run_python_file
from functions.write_file import write_file, schema_write_file


available_functions = types.Tool(
	function_declarations=[schema_get_files_info, 
	schema_get_file_content, 
	schema_run_python_file, 
	schema_write_file,])


#define call_function function to call one of the four functions, it takes function_call_part as input, a types.FunctionCall
def call_function(function_call_part, verbose=False):
	#if verbose is specified, print the function name and args
	if verbose:
		print(f"Calling function: {function_call_part.name}({function_call_part.args})")
	else:
		print(f"Calling function: {function_call_part.name}")
	#add the "working_directory" argument to the dictionary of keyword arguments
	function_call_part.args["working_directory"] = "./calculator"
	#create a dictionary to map function names to functions
	function_map = {
	"get_files_info": get_files_info,
	"get_file_content": get_file_content,
	"run_python_file": run_python_file,
	"write_file": write_file,
	}

	#if the function name is invalid, return a types.Content that explains the error
	if function_call_part.name not in function_map:
		return types.Content(
			role="tool",
			parts=[
				types.Part.from_function_response(
					name=function_call_part.name,
					response={"error": f"Unknown function: {function_name}"},
				)
			],
		)

	#based on the function name, call the function and capture the result
	result = function_map[function_call_part.name](**function_call_part.args)
	#return types.Content with a from_function_response describing the result of the function call
	return types.Content(
		role="tool",
		parts=[
			types.Part.from_function_response(
				name=function_call_part.name,
				response={"result": result},
			)
		],
	)