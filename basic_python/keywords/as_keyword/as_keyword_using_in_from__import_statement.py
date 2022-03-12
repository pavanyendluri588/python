#importing numpy  module with alias name np
import numpy as np
#impoeting the pyplot class from matplotlib and changeing pyplot alias plot
from matplotlib import pyplot as plot

#even_numbers=np.array([2,4,6,8,10,12,14,16,18,12])
even_numbers=np.arange(2,100,2)
print("even_numbers:\n",even_numbers) #printing the even numbers
print("type of even_numbers variable:",type(even_numbers),"\nlenth of even_numbers variable",len(even_numbers))
odd_numbers=np.arange(1,98,2)
print("odd_numbers:\n",odd_numbers) #printing the odd numbers
print("type of odd_numbers variable:",type(odd_numbers),"\nlenth of odd_numbers variable",len(odd_numbers))
multi=even_numbers/odd_numbers
print("multi:\n",multi)
print("type of multi variable:",type(multi),"lenth of multi variable",len(multi))

#ploting 
plot.plot(even_numbers,multi)
plot.title("ploting between evern numbers and multi")
plot.xlabel(even_numbers)
plot.ylabel(multi)
print(plot.show)





