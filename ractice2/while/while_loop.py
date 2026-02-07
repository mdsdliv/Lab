
#1
i = 1
while i < 6:
  print(i)
  i += 1
#2 With the break statement we can stop the loop even if the while condition is true:

#Exit the loop when i is 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#3 With the continue statement we can stop the current iteration, and continue with the next:

Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#4 With the else statement we can run a block of code once when the condition no longer is true:

Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#5
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print("Сумма:", total)


#6
i = 2
while i <= 10:
    print(i)
    i += 2

#7
i = 1
while i <= 10:
    if i % 3 == 0:
        print(i, "делится на 3")
    i += 1

#8
i = 5
while i > 0:
    print(i)
    i -= 1


#9 - total sum 
y= int(input())
tot= 0
i=1 
while i<=y:
    tot+=i
    i+=1
print(tot)
