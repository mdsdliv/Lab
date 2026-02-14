
#1
x = input()
for d in x:
  if d %2 != 0:
    print("Not valid ")
    break 
else: 
  print("Valid")
  # ерекше сандар

#2
n = int(input())
for p in [2,3,5]:
  while n % p ==0:
    n //=p
if n == 1:
  print("Yes")
else: 
  print("No")

#2.1
def isUsual (num):
  for p in [2,3,4]:
    while num % p == 0:
      num//=p
  return num ==1
n = int(input())
if isUsual(n):
  print("Yes")
else:
  print("No")
