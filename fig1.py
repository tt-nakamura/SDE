# reference:
#  D. J. Higham "An Algorithmic Introduction to Numerical
#   Simulation of Stochastic Differential Equations"
#   SIAM Review 43 (2001) 525

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)
T=1; N=500; dt=T/N

W = np.zeros(N+1)
dW = np.random.normal(0, dt**0.5, N)
W[1:] = np.cumsum(dW)

plt.plot(np.linspace(0,T,N+1), W, 'r')
plt.xlim([0,T])
plt.xlabel('t', fontsize=16)
plt.ylabel('W(t)', fontsize=16)

plt.tight_layout()
plt.savefig('fig1.eps')
plt.show()
