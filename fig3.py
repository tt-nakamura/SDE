# reference:
#  D. J. Higham "An Algorithmic Introduction to Numerical
#   Simulation of Stochastic Differential Equations"
#   SIAM Review 43 (2001) 525

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)
lm=2; mu=1; X0=1;
T=1; N=256; dt=T/N; t=np.linspace(0,T,N+1)

W = np.zeros(N+1)
dW = np.random.normal(0, dt**0.5, N)
W[1:] = np.cumsum(dW)

X_exact = X0 * np.exp((lm - mu**2/2)*t + mu*W)
plt.plot(t, X_exact, 'm')

R=4; DT=R*dt; L=N//R
X = np.empty(L+1)
X[0] = X0

for j in range(L):
    DW = np.sum(dW[j*R:(j+1)*R])
    X[j+1] = X[j] + lm*X[j]*DT + mu*X[j]*DW

plt.plot(np.linspace(0,T,L+1), X, 'r--*')
err = X[-1] - X_exact[-1]; print(err)

plt.legend(['exact solution', 'numerical solution'], loc='upper left')
plt.xlim([0,T])
plt.xlabel('t', fontsize=16)
plt.ylabel('X', fontsize=16)
plt.tight_layout()
plt.savefig('fig3.eps')
plt.show()

