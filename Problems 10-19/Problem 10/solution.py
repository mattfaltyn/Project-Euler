import numpy as np
import math
from sympy import *

n = 1
m = 0
while n < 2000000:
  if isprime(n) == True:
    m += n
    n +=1
  else:
    n +=1
print(m)