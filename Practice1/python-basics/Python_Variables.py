#1 
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#2
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#3
x = 5
y = "John"
print(type(x))
print(type(y))

#4
x = "John"
# is the same as
x = 'John'

#5
a = 4
A = "Sally"
#A will not overwrite a

#6
#Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#7 

#Много значений → несколько переменных
x, y, z = "Orange", "Banana", "Cherry"
#Количество переменных = количеству значений.Одно значение → несколько переменных
x = y = z = "Orange"
#Все переменные получают одно и то же значение.Распаковка коллекции (Unpacking)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
#Значения из списка/кортежа присваиваются переменным по порядку


#8  (Global Variables)-Создаётся вне функции.Доступна везде: и внутри функций, и снаружи.

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()  # Python is awesome
#Локальная переменная с тем же именем:Если создать переменную внутри функции с тем же именем, она будет локальной и не изменит глобальную.
Пример:
x = "awesome"

def myfunc():
    x = "fantastic"  # локальная
    print("Python is " + x)

myfunc()  # Python is fantastic
print("Python is " + x)  # Python is awesome
#Ключевое слово global:Позволяет создавать или изменять глобальную переменную внутри функции.
def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)  # Python is fantastic
#Пример изменения глобальной переменной:
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)  # Python is fantastic

#9
