# reference:
#  D. J. Higham "An Algorithmic Introduction to Numerical
#   Simulation of Stochastic Differential Equations"
#   SIAM Review 43 (2001) 525

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)
T=20; M=50000; X0=1
lm=-3; mu=3**0.5
color = ['b', 'r--', 'm-.']

for k in range(3):
    dt = 2**(-k)
    N = int(T/dt)
    X = X0 * np.ones(M)
    X2 = np.empty(N+1); X2[0] = X0**2
    for j in range(N):
        dW = np.random.normal(0, dt**0.5, M)
        X += X*(lm*dt + mu*dW)
        X2[j+1] = np.mean(X**2)

    t = np.linspace(0,T,N+1)
    plt.semilogy(t, X2, color[k],
                 label=r'$\Delta\tau = {}$'.format(dt))

plt.legend()
plt.xlabel('t', fontsize=16)
plt.ylabel('$E(X^2)$', fontsize=16)
plt.xlim([0,T])
plt.tight_layout()
plt.savefig('fig5.eps')
plt.show()
