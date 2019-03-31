# reference:
#  D. J. Higham "An Algorithmic Introduction to Numerical
#   Simulation of Stochastic Differential Equations"
#   SIAM Review 43 (2001) 525

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)
T=1; N=500; dt=T/N; t=np.linspace(0,T,N+1)

M = 1000
W = np.zeros((M, N+1))
dW = np.random.normal(0, dt**0.5, (M,N))
W[:,1:] = np.cumsum(dW, axis=1)
U = np.exp(t + W/2)
U_mean = np.mean(U, axis=0)

plt.plot(t, U_mean, 'b')
plt.plot(t, U[:5].T, 'r--')

print(np.max(np.abs(U_mean - np.exp(9*t/8))))

plt.xlim([0,T])
plt.xlabel('t', fontsize=16)
plt.ylabel('U(t)', fontsize=16)
plt.legend(['mean of 1000 paths', '5 individual paths'])
plt.tight_layout()
plt.savefig('fig2.eps')
plt.show()
