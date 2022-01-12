import numpy as np

x = list(range(1,101))

Y = np.power(x,2)
sumY = sum(Y)

Z = sum(x)
sumZ = pow(Z,2)

print(sumZ-sumY)