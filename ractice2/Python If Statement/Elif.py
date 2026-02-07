#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
#The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.
#sim exam  0
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#1
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
#2
age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")

#3
day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")
#4
x = 15

if x < 10:
    print("Меньше 10")
elif x < 20:
    print("Меньше 20, но больше или равно 10")
else:
    print("20 или больше")

  
