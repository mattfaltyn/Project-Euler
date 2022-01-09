# Create 3 lists (multiples of 3, 5 and 15)
X = list(range(0,1000,3))
Y = list(range(0,1000,5))
Z = list(range(0,1000,15))

# Sum multiples of 3 and 5 while substracting multiples of 15
sum(X)+sum(Y)-sum(Z)