import math

b = 600851475143

def Prime(b):
             while b % 2 == 0:
                         print (2), 
                         b = b / 2 
             for c in range(3,int(math.sqrt(b))+1,2):
                         while b % c == 0:
                                     print (b), 
                                     b = b / c
             if b > 2:
                         print (b) 

Prime(b)

