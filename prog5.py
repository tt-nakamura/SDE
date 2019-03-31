import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)
lm=2; mu=1; X0=1
T=1; N=512; dt=T/N; M=1000

dW = np.random.normal(0, dt**0.5, (N,M))
W = np.sum(dW, axis=0)

X_exact = X0 * np.exp((lm - mu**2/2)*T + mu*W)
X = X0 * np.ones((5,M))

for p in range(5):
    R=2**p; DT=R*dt; L=N//R
    for j in range(L):
        DW = np.sum(dW[j*R:(j+1)*R], axis=0)
        X[p] += X[p]*(lm*DT + mu*DW)

err = np.mean(np.abs(X - X_exact), axis=1)
DT = dt * 2**np.arange(5)
plt.loglog(DT, err, 'b*-')

print(np.polyfit(np.log(DT), np.log(err), 1))

plt.axis([1e-3, 1e-1, 1e-1, 1])
plt.xlabel(r'$\Delta\tau$', fontsize=16)
plt.ylabel('Sample average of $|X(T) - X_L|$', fontsize=16)
plt.tight_layout()
plt.show()
