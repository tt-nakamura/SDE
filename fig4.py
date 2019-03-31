# reference:
#  D. J. Higham "An Algorithmic Introduction to Numerical
#   Simulation of Stochastic Differential Equations"
#   SIAM Review 43 (2001) 525

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)
lm=2; mu=1; X0=1
T=1; N=512; dt=T/N; M=1000

dW = np.random.normal(0, dt**0.5, (N,M))
W = np.sum(dW, axis=0)

X_exact = X0 * np.exp((lm - mu**2/2)*T + mu*W)
X_euler = X0 * np.ones((5,M))
X_milst = np.array(X_euler)

for p in range(5):
    R=2**p; DT=R*dt; L=N//R
    for j in range(L):
        DW = np.sum(dW[j*R:(j+1)*R], axis=0)
        X_euler[p] += X_euler[p]*(lm*DT + mu*DW)
        X_milst[p] += X_milst[p]*(lm*DT + mu*DW + mu**2/2*(DW**2 - DT))

err_euler = np.mean(np.abs(X_euler - X_exact), axis=1)
err_milst = np.mean(np.abs(X_milst - X_exact), axis=1)
DT = dt * 2**np.arange(5)

plt.loglog(DT, err_euler, 'b*-')
plt.loglog(DT, err_milst, 'r+-')

print(np.polyfit(np.log(DT), np.log(err_euler), 1))
print(np.polyfit(np.log(DT), np.log(err_milst), 1))

plt.axis([1e-3, 1e-1, 1e-2, 1])
plt.legend(['Euler-Maruyama', 'Milstein'])
plt.xlabel(r'$\Delta\tau$', fontsize=16)
plt.ylabel('Sample average of $|X(T) - X_L|$', fontsize=16)
plt.tight_layout()
plt.savefig('fig4.eps')
plt.show()
