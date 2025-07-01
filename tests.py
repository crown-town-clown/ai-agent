#import get_files_info from functions
from functions.get_file_content import get_file_content

print('Result for "main.py":')
print(get_file_content("calculator", "main.py"))
print("")

print('Result for "pkg/calculator.py":')
print(get_file_content("calculator", "pkg/calculator.py"))
print("")

print('Result for "/bin/cat": ')
print(get_file_content("calculator", "/bin/cat"))
print("")
