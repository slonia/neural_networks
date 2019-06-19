#! python3
import numpy as np
from urllib.request import urlopen

# x_shape = tuple(map(int, input().split()))
# X = np.fromiter(map(int, input().split()), np.int).reshape(x_shape)
# y_shape = tuple(map(int, input().split()))
# Y = np.fromiter(map(int, input().split()), np.int).reshape(y_shape)

# if (x_shape[1] == y_shape[1]):
#     print(X.dot(Y.T))
# else:
#     print("matrix shapes do not match")


x = np.matrix([[1, 60], [1, 50], [1, 75]])
y=np.matrix([[10],[7],[12]])
b = np.linalg.inv(x.T*x)*x.T*y
print(b)
