# reference:
#  D. J. Higham "An Algorithmic Introduction to Numerical
#   Simulation of Stochastic Differential Equations"
#   SIAM Review 43 (2001) 525

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)
a=2; b=1; T=1; N=200; dt=T/N
X0=1; V0=X0**0.5; c=(4*a-b**2)/8

X = np.empty(N+1); X[0] = X0
V = np.empty(N+1); V[0] = V0

for j in range(N):
    dW = np.random.normal(0, dt**.5)
    X[j+1] = X[j] + (a - X[j])*dt + b*X[j]**.5*dW
    V[j+1] = V[j] + (c/V[j] - V[j]/2)*dt + b/2*dW

t=np.linspace(0,T,N+1)
plt.plot(t, np.sqrt(X), 'b')
plt.plot(t, V, 'ro', fillstyle='none')

print(np.max(np.abs(np.sqrt(X) - V)))

plt.legend(['Direct solution', 'Solution via chain rule'])
plt.xlabel('t', fontsize=16)
plt.ylabel('V(X)', fontsize=16)
plt.xlim([0,T])
plt.tight_layout()
plt.savefig('fig6.eps')
plt.show()
