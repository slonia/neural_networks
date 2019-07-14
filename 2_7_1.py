#! python3
import numpy as np



# def vectorized_forward_pass(self, input_matrix):
#     ones = np.ones((input_matrix.shape[0], 1))
#     example = np.hstack((ones, input_matrix))
#     weights = np.concatenate(([[self.b]], self.w))
#     res = np.dot(example, weights)
#     res = res > 0
#     return res


def train_on_single_example(self, example, y):
    y_pred = int(np.dot(self.w.T, example) + self.b) > 0
    error = y-y_pred
    self.w = self.w + example*error
    self.b = self.b + error



weights=np.array([[1], [0.2], [-0.3]])
example = np.array([[-1], [-2], [-3.5]])
bias = 0.2
y=0
y_pred = int(np.dot(example.T, weights) + bias) > 0
error = y-y_pred
print(y_pred, y)
print(error)
weights = weights + example*error
bias = bias + error
print(weights)
print(bias)
# n — количество примеров,
# m — количество входов.
# Размерность входных данных input_matrix — (n, m),
# размерность вектора весов — (m, 1),
# смещение (bias) — отдельно.
# vectorized_forward_pass должен возвращать массив формы (n, 1),
# состоящий либо из 0 и 1, либо из True и False.


predict = int(np.dot(self.w.T, example)+self.b)>0
error = y-predict
self.w = self.w + error*example
self.b = self.b + error
