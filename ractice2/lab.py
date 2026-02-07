#205 
#Print YES is n is the power of two, else print NO.

# Input
# 16
# Output
# YES
n = int(input())

if n > 0 and (n & (n - 1)) == 0:
    print("YES")
else:
    print("NO")

#206
# Single integer — the maximum in the sequence.

# Input
# 4
# 2 7 3 3
# Output
# 7
n = int(input())
m = max(map(int, input().split()))
print(m)
#second var 
n = int(input())
nums = input().split()
m = int(nums[0])

for x in nums:
    if int(x) > m:
        m = int(x)

print(m)


#207
# Single integer — the position of the maximum in the sequence.

# Input
# 4
# 2 7 3 3
# Output
# 2

n = int(input())
a = list(map(int, input().split()))
print(a.index(max(a)) + 1)
#second var 
n = int(input())
nums = input().split()

mx = int(nums[0])
pos = 1

for i in range(len(nums)):
    if int(nums[i]) > mx:
        mx = int(nums[i])
        pos = i + 1

print(pos)


#208 
# For a given number , print out all the integer powers of two that do not exceed , in increasing order.

# Input format

# Given a positive integer  .

# Output format

# Output the answer for the problem.

# Examples

# Input
# 50
# Output
# 1 2 4 8 16 32 


n = int(input())
x = 1

while x <= n:
    print(x, end=" ")
    x *= 2


#209
# Given an array consisting of integers, write a program that will change all maximal elements to minimal elements of the array. Look at the sample to better understand the conditions.

# Input format

# The first line contains an integer   — array size. The next line contains  integers   — elements of the array.

# Output format

# Array with changed elements.

# Examples

# Input
# 3
# 9 5 5
# Output
# 5 5 5 
n = int(input())
nums = input().split()

# Найдём минимум и максимум
mn = mx = int(nums[0])
for x in nums:
    x = int(x)
    if x > mx:
        mx = x
    if x < mn:
        mn = x

# Выведем с заменой
for x in nums:
    x = int(x)
    if x == mx:
        x = mn
    print(x, end=" ")
#second var 
n = int(input())
a = list(map(int, input().split()))

mx = max(a)
mn = min(a)

for i in range(n):
    if a[i] == mx:
        a[i] = mn

print(*a)

#210
# The first line contains an integer   — array size. The next line contains  integers   — elements of the array.

# Output format

# Sorted array in reversed order.

# Examples

# Input
# 9
# 4 11 1 7 5 1 6 10 8
# Output
# 11 10 8 7 6 5 4 1 1 
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
print(*a)

#sec var 
n = int(input())
nums = input().split()

# Преобразуем в числа
for i in range(n):
    nums[i] = int(nums[i])

# Простая сортировка по убыванию (пузырьком)
for i in range(n):
    for j in range(i+1, n):
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

# Вывод
for x in nums:
    print(x, end=" ")


#211
# You’re given an array consisting of integers. Write a program that will reverse elements on the interval between positions  and .

# Input format

# The first line contains three integers , , ,  — array size and positions  and . The next line contains  integers   — elements of the array.

# Output format

# Array with reversed elements between positions  and .

# Examples

# Input
# 5 2 5
# 2 8 10 5 12
# Output
# 2 12 5 10 8 

# n - размер массива, l и r - позиции
n, l, r = map(int, input().split())
nums = input().split()

# l и r даны с 1, преобразуем в индексы Python
l -= 1
r -= 1

# Выведем массив с переворотом на отрезке
for i in range(n):
    if l <= i <= r:
        print(nums[r - (i - l)], end=" ")
    else:
        print(nums[i], end=" ")
#sec var
n, l, r = map(int, input().split())
a = list(map(int, input().split()))

# переворот от l до r (индексы с 0)
a[l-1:r] = a[l-1:r][::-1]

print(*a)



#212
# Given an array of  integers, output the square value of each element.

# Input format

# The first line contains the integer   — array size. The next line contains  integers   — elements of the array.

# Output format

# Changed array.

# Examples

# Input
# 5
# 6 7 15 6 11
# Output
# 36 49 225 36 121 

n = int(input())
nums = input().split()

for x in nums:
    x = int(x)
    print(x**2, end=" ")

#sec var 
n = int(input())
a = list(map(int, input().split()))

for x in a:
    print(x**2, end=" ")
#3var 
n = int(input())
a = list(map(int, input().split()))
print(*[x**2 for x in a])



#213
# Given a single number  check if it is a prime or not. A prime is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.

# Input format

# Single integer  .

# Output format

# Yes if it is prime; No otherwise.

# Examples

# Input
# 48
# Output
# No

n = int(input())

if n <= 1:
    print("No")
else:
    is_prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            break
    print("Yes" if is_prime else "No")




#214
# The first line contains an integer  (), representing the number of elements.

# The next line contains  integers, where each integer  satisfies .

# Output format

# A single integer representing the most frequent element. If multiple elements have the same frequency, output the smallest one.

# Examples

# Input
# 7
# 4 2 4 3 2 4 3
# Output
# 4
# Input
# 6
# 4 1 2 3 3 1
# Output
# 1
n = int(input())
nums = input().split()

freq = {}
for x in nums:
    x = int(x)
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

# Найдём элемент с максимальной частотой, если несколько — минимальный
max_count = 0
ans = None
for k in freq:
    if freq[k] > max_count or (freq[k] == max_count and k < ans):
        max_count = freq[k]
        ans = k

print(ans)
#2var 
n = int(input())
a = list(map(int, input().split()))

freq = {}
for x in a:
    freq[x] = freq.get(x, 0) + 1

# Минимальный элемент с максимальной частотой
print(min(k for k,v in freq.items() if v == max(freq.values())))





#215
# Professor of Programming Principles always checks the presence of students using WSP. But today the WSP is down, so everyone must write his own surname at the attendance list.

# But some students may have written their surname more than one times. That’s why professor asked for you help. You should count the number of unique surnames in the list.

# Input format

# The first line of input contains a number  - number of students’ surnames . Each of the next  lines contains a students surname  .

# Output format

# Print the number of unique surnames.

# Examples

# Input
# 5
# Baisakov
# Akshabayev
# Mukhsimbayev
# Amanov
# Akshabayev
# Output
# 4
# Input
# 4
# SomeSurname
# SomeOtherSurname
# SomeReallylongSurname
# sOMEiNVERSEDsURNAME
# Output
# 4
# Input
# 3
# NotASurname
# NotASurname
# NotASurname
# Output
# 1


n = int(input())
unique = set()

for _ in range(n):
    surname = input()
    unique.add(surname)

print(len(unique))

#2var
n = int(input())
surnames = [input() for _ in range(n)]
print(len(set(surnames)))


#216
# The element of the array is called a  if there was no same element in the array before.

# For every element of the array, print “YES” if it is a newbie, and “NO” otherwise.

# Input format

# The first line of input contains an integer  . The next line contains  integers — elements of the array  .

# Output format

# For every element of the array, print “YES” if it is a newbie, and “NO” otherwise.

# Examples

# Input
# 6
# 1 4 10 4 1 9
# Output
# YES
# YES
# YES
# NO
# NO
# YES

n = int(input())
nums = input().split()
seen = set()

for x in nums:
    if x in seen:
        print("NO")
    else:
        print("YES")
        seen.add(x)


#2var
n = int(input())
a = list(map(int, input().split()))
seen = set()

for x in a:
    if x in seen:
        print("NO")
    else:
        print("YES")
        seen.add(x)


#217
# Sanzhar have n telephone numbers in his contact list. Your task is to find how many numbers occurs in contact list exactly three times.

# Input format

# First line contains one integer number n.(1<=n<=1000) Next n lines contains telephone numbers. Each telephone number has 14 symbols

# Output format

# Print the number of telephone numbers which occurs exactly three times in Sanzhar’s contact list.

# Examples

# Input
# 3
# +7707707707707
# +7707707707707
# +7707707707707
# Output
# 1
n = int(input())
freq = {}

for _ in range(n):
    num = input()
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

count = 0
for v in freq.values():
    if v == 3:
        count += 1

print(count)


#2var
n = int(input())
nums = [input() for _ in range(n)]

freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1

print(sum(1 for v in freq.values() if v == 3))



#218
# You have array which contains n strings, for each string S in our array output first entry of S in the given array(in index).

# Input format

# First line contains one integer number n -size of the array, and next n lines contain n strings of the array.(1<=n<=20)

# Output format

# For each string S output first entry of S in the given array.(Print strings in lexicographical order)

# Examples

# Input
# 3
# ab
# ab
# cd
# Output
# ab 1
# cd 3


n = int(input())
first_index = {}

for i in range(1, n+1):
    s = input()
    if s not in first_index:
        first_index[s] = i

# Выводим в лексикографическом порядке
for s in sorted(first_index):
    print(s, first_index[s])
#2var 
n = int(input())
a = [input() for _ in range(n)]

first_index = {}
for i, s in enumerate(a, 1):
    if s not in first_index:
        first_index[s] = i

for s in sorted(first_index):
    print(s, first_index[s])


#219 
# Aida is a very good girl, but there is one thing, she is fond of doramas (Korean TV serials). Every day she watches several episodes of some dorama. For each dorama, print how many episodes of this dorama in total she watched in n days. Output the doramas and the number of episodes (print doramas in lexicographical order )

# Input format

# First line contains the number of days n <= 100 Next n lines contain one string s and one integer number k, where s - name of the dorama (s.size() < 30) and k - number of episodes.

# Output format

# In each line print name of the dorama and numbers of episodes(print doramas in lexicographically order)

# Examples

# Input
# 5
# HundredMillionStarsFromTheSky 10
# WhereStarsLand 14
# WhereStarsLand 4
# TheThirdCharm 100
# HusbandForHundredDays 1
# Output
# HundredMillionStarsFromTheSky 10
# HusbandForHundredDays 1
# TheThirdCharm 100
# WhereStarsLand 18


n = int(input())
episodes = {}

for _ in range(n):
    line = input().split()
    name = line[0]
    k = int(line[1])
    if name in episodes:
        episodes[name] += k
    else:
        episodes[name] = k

# Вывод в лексикографическом порядке
for name in sorted(episodes):
    print(name, episodes[name])


#2var 
n = int(input())
episodes = {}

for _ in range(n):
    name, k = input().split()
    k = int(k)
    episodes[name] = episodes.get(name, 0) + k

for name in sorted(episodes):
    print(name, episodes[name])


#220
# Do you know what is MongoDB? No? It is a document based key-value database. But what is it document and what does it mean “key-value database”? Okay, let’s explore this on the example.

# Imagine you have an empty document. You can insert some key-value pair to this document. However the keys in the document must be unique. So, if you want to insert a new key-value pair and there is already some pair with same key in the document, the value is replaced by a new one.

# Also, you can get a value by specifying the key, if such key exists.

# So your task is to emulate one document of the MongoDB. Initially, you have an empty documents, and you will be given  commands. There is two types of the commands:

# “set key value” - this command requires you to “add” to the document a new “key” - “value” pair.

# “get key” - this command requires you to print the value associated with the given “key”, if such key exists. Otherwise, you should print “KE: no key <KEY> found in the document”, where <KEY> should be replace by a given key.

# Input format

# The first line of input contains an integer  - the number of commands . Each of the next  lines contains one of the two types of commands.

# Output format

# For each “get” command, print the value associated with given key (or an error in a format specified in the statements if there is no such key in the “document”).

# Examples

# Input
# 10
# set s0m3_c001_k3y s0m3_c001_v41u3
# set some_key some_other_value
# get some_key
# get no_key
# set no_key no_value
# get no_ke
# get s0m3_c001_k3y
# set s0m3_c001_k3y some_value
# get s0m3_c001_k3y
# get xx_key
# Output
# some_other_value
# KE: no key no_key found in the document
# KE: no key no_ke found in the document
# s0m3_c001_v41u3
# some_value
# KE: no key xx_key found in the document
# Input
# 6
# get aaa
# get bbb
# get ccc
# set aaa sm_vl
# get aa
# get aaa
# Output
# KE: no key aaa found in the document
# KE: no key bbb found in the document
# KE: no key ccc found in the document
# KE: no key aa found in the document
# sm_vl



n = int(input())
document = {}

for _ in range(n):
    cmd = input().split()
    if cmd[0] == "set":
        key = cmd[1]
        value = cmd[2]
        document[key] = value
    elif cmd[0] == "get":
        key = cmd[1]
        if key in document:
            print(document[key])
        else:
            print(f"KE: no key {key} found in the document")


#2var 
n = int(input())
document = {}

for _ in range(n):
    cmd = input().split()
    if cmd[0] == "set":
        document[cmd[1]] = cmd[2]
    elif cmd[0] == "get":
        print(document.get(cmd[1], f"KE: no key {cmd[1]} found in the document"))



#косымша бауры 
n = int(input())  # сколько чисел
total = 0
for _ in range(n):
    x = int(input())  # ввод каждого числа
    total += x
print(total)
