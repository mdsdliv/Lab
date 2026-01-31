#1

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'complex'>

#2Преобразование типов (Type Conversion):
x = 1       # int
y = 2.8     # float
z = 1j      # complex

a = float(x)   # int → float
b = int(y)     # float → int
c = complex(x) # int → complex
# Complex → int/float нельзя.

#3
import random
print(random.randrange(1, 10))  # случайное число от 1 до 9
#4
z1 = 2 + 3j
z2 = 1 - 1j
z_sum = z1 + z2
z_mul = z1 * z2
print(z_sum)  # 3+2j
print(z_mul)  # 5+1j

#5
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
