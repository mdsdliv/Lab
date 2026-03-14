
#МОИ КОСЯКИ  

#Найти возраст
birth_year = int(input())
current_year = int(input())

age = current_year - birth_year
print(age)


#Найти количество положительных делителей числа
n = int(input())

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

print(count)


#В массиве найти наименьшее положительное число, если положительных нет — вывести -1
n = int(input())
arr = list(map(int, input().split()))

mn = -1

for x in arr:
    if x > 0:
        if mn == -1 or x < mn:
            mn = x

print(mn)


# сумма чисел 
n = int(input()
s =0 
for i in range(1,n+1):
  s +=i
print(s)

# WHile когда не знаем сколько раз - сколько цифр в числе ?

n = int(input())
s =0 
while 0<n :
  s += 1
  n//=10
print(s)

# прочитать с 1 до н

n = int(input())
i =1 
while i<=n:
   print(i)
  i+=1

# напечатать таблицу 
n = int(input())
for i in range(1,n+1):
    print(1*2)


#LIST

#ввод массива 
arr = ist(map(int,input().split()))
#пройтись по массиву 
for x in arr:
  print(x)
#найти минимальный 

g = arr[0]
arr= list(map(int,input().split()))
for x in range:
  if x < g:
    g = x
print(g)



# FUNCTIONS

def square(x):
  return x*x
x = int(input())
print(square(ax)

#сумма массиыв через функцию 
def sum(arr):
  d = 0
  for x in range:
    d+=x
  return d
arr=list(map(int,input().split()))
print(sum(arr)) 


#603
n = int(input())
arr =list(map(str,input().split()))
for i, x in enumerate(arr):
    print(f"{i}:{x}", end=" ")

#604  ZIPPP
n = int(input())
a =list(map(int,input().split()))

b =list(map(int,input().split()))
d =0
for x, y in zip(a,b):
    d += x*y
    
print(d)



#604

a = input()
v = "aeoiuAEOIU"
for ch in a:
    if ch in v:
        print("Yes")
        break 
else:
    print("No")
##########################
a = input()
v = "aeoiuAEOIU"

if any(ch in v for ch in a):
        print("Yes")
else:
    print("No")


#607
a = int(input())
arr= list(map(str,input().split()))
print(max(arr,key=len))

#608 
 a = int(input())
arr= list(map(int,input().split()))
s =set(arr)
res=sorted(s)
print(*res)

#609
a = input()
arr= list(map(str,input().split()))
red= list(map(str,input().split()))
d = input()
l=0

for x, y in zip(arr,red):
    if d in x:
        print(y)
        break
else:
    print("Not found")
#610
a = input()
arr= list(map(int,input().split()))
l=0

for x in arr:
    if x != 0:
        l +=1
    else:
        continue 
print(l)


# 4LABBB::::
#1 
def sp(n):
    for i in range(1,n+1):
        yield i*i
    
n = int(input())
for x in sp(n):
    print(x)

#2
n = int(input())
for x in range(0, n+1):
    if x % 2 == 0:
        if x != 0:
            print(",", end="")
        print(x, end="")

#####################################
def gen(n):
    for i in range(0,n+1,2):
        yield i
n = int(input())
print(*gen(n),sep=",")


#3
def gen(n):
    for i in range(0,n+1):
        if i%3 == 0 and i%4==0:
            yield i
n = int(input())
print(*gen(n),sep=",")


#4
def gen(a,b):
    for i in range(a,b+1):
        yield i *i
        
a, b= map(int,input().split())
for x in gen(a,b):
    print(x)

#5
def gen(n):
  for i in range(n,-1,-1):
    yield i
n = int(input())
for x in gen(n):
  print(x)

#6 ФИБОНАЧИИИИИИИИИИИИИИИИИИИИИИИИИИИИИ

def gen(n):
    a =0 
    b =1

    for i in range(0, n+1):
            yield a
            c = a+b
            a =b
            b=c
            
n = int(input())
print(*gen(n),sep=",")


###### 7 - делительность на других чисел 
def gen(n):
    for i in range(2, n+1):
        ok = True 
        for j in range(2,int(i*0.5)+1):
            if i % j ==0:
                ok = False
                break 
        if ok:
            yield i

n = int(input())
print(*gen(n))



###########8
def gen(n):
    l =2
  
   
    for i in range(0,n+1):
        yield l**i
n = int(input())
print(*gen(n))


############9
d = input().split()
n = int(input())
for j in range(n):
    for x in d:

        print(x,end=" " )


############10
import math
a,b,c = map(int,input().split())
d = b**2-4*a*c
print(f"{d: .1f} {math.sqrt(d): .1f}")

#############11
from datetime import datetime

start = datetime.strptime(input(), "%Y-%m-%d")
other = datetime.strptime(input(), "%Y-%m-%d")

print((other - start).days)

#########12
from datetime import datetime

start = datetime.strptime(input(), "%Y-%m-%d")

while True:
    try:
        d = datetime.strptime(input(), "%Y-%m-%d")
        print((d - start).days)
    except:
        break

