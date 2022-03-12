import numpy as np
x=[[1,2,3,4,5],
  [11,22,33,44,55],
  [6,7,8,9,10]]
class layer_dense:
     def __init__(self,n_inputs,n_neurons):
          self.weights=np.random.randn(n_inputs,n_neurons)
          self.biases=np.zeros((1,n_neurons))
     def forword(self,input):
          self.output=np.dot(input,self.weights)+self.biases
          print(self.output)
layer1=layer_dense(5,3)
layer1.forword(x)
layer2=layer_dense(3,2)
layer2.forword(layer1.output)

