#! python3
import numpy as np

x=np.array([2, 4.0, 5.0, 4,1,2]).reshape(3, 2)
print(x.shape)
w = np.array([[1], [2.0], [3]])
print(w.shape)
print(w.T.dot(x).T)
