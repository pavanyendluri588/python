import numpy as np
#checking the version of the numpy
print("nnumpy version:",np.__version__)
#creating arrat 
arr=np.array([1,2,3,4,5])
#printing the array
print("arr:",arr)
#printing  array shape
print(arr.shape)
#getting the memory location of array
print(arr.data)
#totla no of elements in array
print(arr.size)
#this will return the bytes of array datatype
print(arr.itemsize)
#printing the array data type
print(arr.dtype)
#printing the type of the array
print(type(arr))
#printing the dimensions of array
print(arr.ndim)
print("=====================================================")
print("0-D array:")
arr1=np.array(41)
print("array",arr1)
print("dimensuons of the array:",arr1.ndim)
print("shape of the array:",arr1.shape)
print("checking this id copy or view:",arr1.base)

print("===================================================")
print("1-D array:")
arr1=np.array([1,2,3,4])
print("array",arr1)
print("dimensuons of the array:",arr1.ndim)
print("shape of the array:",arr1.shape)
print("checking this id copy or view:",arr1.base)

print("2-D array:")
arr1=np.array([[5,4,3,2,1],[1,2,3,4,5]])
print("array",arr1)
print("dimensuons of the array:",arr1.ndim)
print("shape of the array:",arr1.shape)
print("checking this id copy or view:",arr1.base)

print("===========================================================")
print("3-D array:")
arr1=np.array([[[1,2,3,4],[9,8,7,6]],[[9,8,7,5],[5,4,3,1]]])
print("array",arr1)
print("dimensuons of the array:",arr1.ndim)
print("shape of the array:",arr1.shape)
print("checking this id copy or view:",arr1.base)