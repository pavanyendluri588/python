import numpy as np
print("converting list to array")
print("single list")
list1=[1,2,3,4,5,6]
print("list1\n",list1)
print("type(list1)\n",type(list1))
arrayl1=np.asarray(list1)
print("array1:\n",arrayl1)
print("type(array1):\n",type(arrayl1))

print("=============================================")
print("num int to array:")
num1=23
print("num1:\n",num1)
print("type(num1):\n",type(num1))
array_n_i1=np.asarray(num1)
print("array_n_i1:\n",array_n_i1)
print("type(array_n_i1):",type(array_n_i1))
print("=========")
print("num float to array:")
float1=56.5
print("float1:\n",float1)
print("type(float1):\n",type(float1))
array_n_f1=np.asarray(float1)
print("array_n_f1:\n",array_n_f1)
print("type(array_n_f1):\n",type(array_n_f1))
print("========")
print("num complex to array")
complex1=33+7j
print("complex1:\n",complex1)
print("type(complex1):",type(complex1))
array_n_c1=np.asarray(complex1)
print("array_n_c1:\n",array_n_c1)
print("type(array_n_c1):\n",type(array_n_c1))
print("===========================================")
print("string to array:")
str1="string1"
print("str1:\n",str1)
print("type(str1):",type(str1))
array_n_s1=np.asarray(str1)
print("array_n_s1:\n",array_n_s1)
print("type(array_n_s1):\n",type(array_n_s1))

print("===========================================")
print("tuple to array")
tuple1={1,2,3,4,5,}
print("tuple1:\n",tuple1)
print("type(tuple1)",type(tuple1))
array_t1=np.array(tuple1)
print("array_t1:\n",array_t1)
print("type(array_t1):\n",type(array_t1))
print("===========================================")
print("dictonary to array")
dict1={1:5,2:3,3:2,4:5,5:8}
print("dict1:\n",dict1)
print("type(dict1)",type(dict1))
array_d1=np.array(dict1)
print("array_d1:\n",array_d1)
print("type(array_d1):\n",type(array_d1))
print("===========================================")
print()
