#import get_files_info from functions
from functions.run_python import run_python_file

print('Result for "main.py":')
print(run_python_file("calculator", "main.py"))
print("")

print('Result for "tests.py":')
print(run_python_file("calculator", "tests.py"))
print("")

print('Result for "../main.py": ')
print(run_python_file("calculator", "../main.py"))
print("")

print('Result for "nonexistent.py": ')
print(run_python_file("calculator", "nonexistent.py"))
print("")