#! python3
import urllib
from urllib import request
import numpy as np

Y = np.array([1.0, 1.0, 0.0])
weights = np.array([0.0, 0.0, 0.0])
X = np.array([
    [1, 1, 0.3],
    [1, 0.4, 0.5],
    [1, 0.7, 0.8]])
perfect = False
while perfect == False:
    perfect = True
    for x in range(3):
        example = X[x]
        predict = int(np.dot(example, weights) > 0)
        if predict != Y[x]:
            perfect = False
            if predict == 0.0:
                weights += example
            else:
                weights -= example
print(" weights: ", weights)

