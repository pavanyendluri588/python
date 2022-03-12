import numpy as np
import pandas as pd
import sys
import matplotlib
print("python version:",sys.version)
print("numpy version:",np.__version__)
print("pandas version:",pd.__version__)
print("matplotlib varsion:",matplotlib.__version__)
input=[1.2,1.5,2.7]
weights=[3.1,3.2,3.3]

bias=3.5
output=input[0]*weights[0]+input[1]*weights[1]+input[2]*weights[2]+bias
print(output)
