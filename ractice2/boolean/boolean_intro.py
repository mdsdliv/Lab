#Boolean Values
#short exam
print(10 > 9)
print(10 == 9)
print(10 < 9)

#1
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#2
print(bool("Hello"))
print(bool(15)) # оценит пуста или нет 

#3Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())

#3.1
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#3.2 Проверка, является ли объект целым числом:
x = 200
print(isinstance(x, int))

#4
#is 	Returns True if both variables are the same object	x is y	
#is not	Returns True if both variables are not the same object

#5
#Check if "banana" is present in a list:

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

#Check if "pineapple" is NOT present in a list:

fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)
