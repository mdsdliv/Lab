
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

№3
s = input().strip()

to_digit = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
}
to_triplet = {v: k for k, v in to_digit.items()}

# 1) найти оператор
op_pos = -1
op = ""
for i, ch in enumerate(s):
    if ch in "+-*":
        op_pos = i
        op = ch
        break

a_str = s[:op_pos]
b_str = s[op_pos+1:]

# 2) декод (строка из триплетов -> int)
def decode(t):
    digits = []
    for i in range(0, len(t), 3):
        trip = t[i:i+3]
        digits.append(to_digit[trip])
    return int("".join(digits)) if digits else 0

a = decode(a_str)
b = decode(b_str)

# 3) посчитать
if op == "+":
    res = a + b
elif op == "-":
    res = a - b
else:
    res = a * b

# 4) энкод (int -> строка триплетов)
sign = ""
if res < 0:
    sign = "-"
    res = -res

out = "".join(to_triplet[d] for d in str(res))
print(sign + out)


#3.1 
s = input()

m = {"ZER":"0","ONE":"1","TWO":"2","THR":"3","FOU":"4",
     "FIV":"5","SIX":"6","SEV":"7","EIG":"8","NIN":"9"}

r = {v:k for k,v in m.items()}

# заменяем триплеты на цифры
for k,v in m.items():
    s = s.replace(k, v)

# считаем выражение
ans = str(eval(s))

# возвращаем цифры в триплеты
print("".join(r[d] for d in ans if d != "-"))

