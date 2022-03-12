"""
To read a file in Python, we must open the file in reading r mode.

There are various methods available for this purpose. We can use the read(size) method to read in the size number of data. If the size parameter is not specified, it reads and returns up to the end of the file.

We can read the text.txt file we wrote in the above section in the following way:

>>> f = open("test.txt",'r',encoding = 'utf-8')
>>> f.read(4)    # read the first 4 data
'This'

>>> f.read(4)    # read the next 4 data
' is '

>>> f.read()     # read in the rest till end of file
'my first file\nThis file\ncontains three lines\n'

>>> f.read()  # further reading returns empty sting
''
We can see that the read() method returns a newline as '\n'. Once the end of the file is reached, we get an empty string on further reading.

We can change our current file cursor (position) using the seek() method. Similarly, the tell() method returns our current position (in number of bytes).

>>> f.tell()    # get the current file position
56

>>> f.seek(0)   # bring file cursor to initial position
0

>>> print(f.read())  # read the entire file
This is my first file
This file
contains three lines
We can read a file line-by-line using a for loop. This is both efficient and fast.

>>> for line in f:
...     print(line, end = '')
...
This is my first file
This file
contains three lines
In this program, the lines in the file itself include a newline character \n. So, we use the end parameter of the print() function to avoid two newlines when printing.

Alternatively, we can use the readline() method to read individual lines of a file. This method reads a file till the newline, including the newline character.

>>> f.readline()
'This is my first file\n'

>>> f.readline()
'This file\n'

>>> f.readline()
'contains three lines\n'

>>> f.readline()
''
Lastly, the readlines() method returns a list of remaining lines of the entire file. All these reading methods return empty values when the end of file (EOF) is reached.

>>> f.readlines()
['This is my first file\n', 'This file\n', 'contains three lines\n']
"""
file=open(r"D:\INT_213_Python\basic_python\file_handleing\file_access_modes\read_mode\file.txt","r+")
print("=================================================================================================")
print("file.read():\n",file.read())
print("=================================================================================================")
print("file.read(4):\n",file.read(4))
print("=================================================================================================")
print("file.tell():\n",file.tell())
print("=================================================================================================")
print("file.seek(50):\n",file.seek(50))
print("=================================================================================================")
print("printing the file line by line using the for loop:\n")
c=0
for line in file:
   c+=1
   print("line[",c,"]:\n",line) #printing the file line by line using the for loop
print("the file cointains ",c," lines")
print("================================================================================================")
#checking if the file is in write mode or not
if file.writable():
   print("File is write mode")
else:
   print("File is not in write")
print("==================================================================================================")
print("file.readlines():\n",file.readlines())
#writing into the file
"""
file1.writelines(file) #copying the things

"""