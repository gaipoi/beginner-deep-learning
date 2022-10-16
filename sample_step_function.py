import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y_step = step_function(x)
y_sigmoid = sigmoid(x)
plt.plot(x, y_sigmoid)
plt.plot(x, y_step, linestyle = "--")
# y軸の範囲の指定
plt.ylim(-0.1, 1.1)
plt.show()



