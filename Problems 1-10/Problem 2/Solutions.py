def fib(n):
  if n<2:
    return 1
  else:
    res = fib(n-1) + fib(n-2)
    return res

n=33
sum = 0
for i in range(0, n):
    r = fib(i)
    if r % 2 == 0:
      sum += r

print(sum)

