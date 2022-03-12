"""
In order to write into a file in Python, we need to open it in write w, append a or exclusive creation x mode.

We need to be careful with the w mode, as it will overwrite into the file if it already exists. Due to this, all the previous data are erased.

Writing a string or sequence of bytes (for binary files) is done using the write() method. This method returns the number of characters written to the file.

with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
This program will create a new file named test.txt in the current directory if it does not exist. If it does exist, it is overwritten.

We must include the newline characters ourselves to distinguish the different lines.


"""
#this python program is used to write iin the file 
file=open(r"D:\INT_213_Python\basic_python\file_handleing\file_access_modes\write_mode\output_of_writing_to_files_in_python.txt",'w+')
file.write("this is pavan rram chandar\n")
file.write("i am from vijayawada\n")
file.write("this file is writing in the lenova laptop\n")
file.write("now time is full")