#1. File and path operations
(работа с файлами и путями)
os
старый, но базовый модуль
os.remove() → удалить файл
os.rename() → переименовать
os.path.exists() → проверить существует ли файл
os.getcwd() → где ты сейчас (текущая папка)
os.chdir() → перейти в другую папку


#shutil
#более “мощный”, для операций с файлами
shutil.copy() → копировать файл
shutil.move() → переместить файл
shutil.rmtree() → удалить папку полностью (даже если внутри есть файлы)
пример:
import shutil
shutil.copy("a.txt", "b.txt")


#pathlib
#новый, самый удобный способ (лучше юзать его)
from pathlib import Path

p = Path("demofile.txt")

print(p.exists())   # есть ли файл
print(p.name)       # имя файла
print(p.suffix)     # расширение


#2. Directory management
#(управление папками)
os.mkdir("test") → создать папку
os.makedirs("a/b/c") → создать сразу вложенные папки
os.listdir() → список файлов в папке
os.chdir("path") → перейти в папку
os.getcwd() → узнать текущую папку
os.rmdir("test") → удалить пустую папку
пример:
import os

os.mkdir("new_folder")
print(os.listdir())









#3. Built-in functions
(встроенные функции — очень часто в тестах)
базовые:
len([1,2,3]) → 3
sum([1,2,3]) → 6
min([1,2,3]) → 1
max([1,2,3]) → 3
map()
#применяет функцию ко всем элементам
nums = [1,2,3]
res = list(map(lambda x: x*2, nums))
# [2,4,6]



filter()
#фильтрует по условию
nums = [1,2,3,4]
res = list(filter(lambda x: x % 2 == 0, nums))
# [2,4]



reduce()
#сворачивает в одно значение
from functools import reduce

nums = [1,2,3]
res = reduce(lambda x,y: x+y, nums)
# 6


enumerate()
даёт индекс + значение
a = ["a","b","c"]
for i, v in enumerate(a):
    print(i, v)


zip()
склеивает списки
a = [1,2]
b = ["a","b"]

print(list(zip(a,b)))
# [(1,'a'), (2,'b')]



sorted()
сортировка
a = [3,1,2]
print(sorted(a))  # [1,2,3]



приведение типов:
int("5")
float("3.14")
str(123)
list("abc")



Итог 
os → базовая работа с файлами/папками
shutil → копировать/двигать/удалять папки
pathlib → современный удобный вариант
built-in → это просто функции, которые ты юзаешь всегда
