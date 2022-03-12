"""
in  terminal:
PS D:\INT_213_Python\python_exercise1> python -V
Python 3.9.7
PS D:\INT_213_Python\python_exercise1> python --version
Python 3.9.7

"""
#printing python version for that we use sys module
import sys
print("python version:",sys.version)
print("type(sys.version)",type(sys.version))
#printing the python version as tuple for that we use platform module
import platform
print("python version as tuple:",platform.python_version_tuple())
#checking
print("checking the version datatype",type(platform.python_version_tuple()))