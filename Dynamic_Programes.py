def f(n):
  if n<=1: return n
  return f(n-1) + f(n-2)
  
print(f(100))

def f2(n,memory={}):
  if n in memory:return memory[n]
  if n <= 1: return n
  memory[n] = f2(n-1,memory) + f2(n-2,memory)
  return memory[n]
  
s = f2(400)
print(len(str(s)),s)

def under_f(n):
  if n <= 1:return n
  dp = [0] * (n+1)
  dp[1] = 1
  for i in range(2,n+1):
    dp[i] = dp[i-1]+dp[i-2]
  return dp[n]
  
print(under_f(400))