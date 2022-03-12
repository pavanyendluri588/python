"""
r means raw the raw string cam handle the backslashes in the file path
A raw string will handle back slashes in most cases, such as these two examples:

In [11]:
r'c:\path'

Out[11]:
'c:\\path'
"""
#to send output into file 
"""
import sys
 
path = 'path/to/some/dir/file.txt'
sys.stdout = open(path, 'w')
"""
import sys
path=r"D:\INT_213_Python\basic_python\file_handleing\file_access_modes\output_for_read_mode.txt"
sys.stdout=open(path,'w')
 
print("=============================================================================")
#opening the file in the read mode in the current directory
print("<<<opening the file in the read mode in the current directory>>>>")
input_file_in_read_mode=open(r"D:\INT_213_Python\basic_python\file_handleing\file_access_modes\file.txt","r")
#print(input_file_in_read_mode.read())
#checking if the file open
if input_file_in_read_mode:
   print("File is opened successfully in the read mode")
#closeing the file
input_file_in_read_mode.close()
#checking if the file is closed successfully
if  input_file_in_read_mode.closed:
    print("File is closed successfully")
print("===============================================================================")
#opening the file in read only in the binary format
print("<<<opening the file in read only in the binary format>>>")
input_file_in_read_mode_in_binary_format=open(r"D:\INT_213_Python\basic_python\file_handleing\file_access_modes\file.txt","rb")
#print(input_file_in_read_mode_in_binary_format.read())
#checking if the file open
if input_file_in_read_mode_in_binary_format:
    print("File is opened in successfully in the read mode in the binary format")
#closeing the file
input_file_in_read_mode_in_binary_format.close()
#checking the file if closed or not
if input_file_in_read_mode_in_binary_format.closed:
   print("File is closed successfully")
print("===============================================================================")
#opening the file in the read and write mode
print("<<<opening the file in the read and write mode>>>")
input_file_in_read_and_write_mode=open(r"D:\INT_213_Python\basic_python\file_handleing\file_access_modes\file.txt","r+")
#printing the contents in the file
#print(input_file_in_read_and_write_mode.read())
#checking if the file open
if input_file_in_read_and_write_mode:
   print("File is successfully in the read and write mode")
#closeing the file:
input_file_in_read_and_write_mode.close()
if input_file_in_read_and_write_mode.closed:
   print("File is closed successfully")
print("===============================================================================")
#opening the file in the read and write mode in the binary format
print("<<<opening the file in the read and write mode in the binary format>>>")
input_file_in_read_and_write_mode_in_binary_format=open(r"D:\INT_213_Python\basic_python\file_handleing\file_access_modes\read_and_write_mode _in_binary_format.txt","rb+")
#printing the contents in the file
#print(input_file_in_read_and_write_mode_in_binary_format.read())
#checking if the file open
if input_file_in_read_and_write_mode_in_binary_format:
   print("File is successfully in the read and write mode in the binary format")
#closeing the file:
input_file_in_read_and_write_mode_in_binary_format.close()
if input_file_in_read_and_write_mode_in_binary_format.closed:
   print("File is closed successfully")
print("===============================================================================")
"""
#copying the file
import shutil as file_copy_module
destination="D:\INT_213_Python\basic_python\	file_handleing\file_access_modes\file(copy).txt"
file1=file_copy_module.copyfile(input_file,destination)
"""


