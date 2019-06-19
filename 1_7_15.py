#! python3
import urllib
from urllib import request
import numpy as np

from urllib.request import urlopen
f = urlopen('https://stepic.org/media/attachments/lesson/16462/boston_houses.csv')
# fname = input()  # read file name from stdin
# f = urllib.request.urlopen(fname)  # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with

Y = np.matrix([data[..., 0]]).T
X = np.matrix(data)
X[..., 0] = np.ones(Y.shape)
B = np.linalg.inv(X.T*X)*X.T*Y
B = np.asarray(B)
for i in B:
    print(*i, end = ' ')
