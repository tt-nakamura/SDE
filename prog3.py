import numpy as np

np.random.seed(100)
T=1; N=500; dt=T/N

dW = np.random.normal(0, dt**0.5, N)
W = np.cumsum(dW)

ito = np.dot(W[:-1], dW[1:])
print(ito, ito - (W[-1]**2 - T)/2)
