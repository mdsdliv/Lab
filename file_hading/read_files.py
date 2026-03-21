#Если файл находится в другом месте, вам нужно будет указать полный путь к нему:
f = open("D:\\myfiles\\welcome.txt")
print(f.read())

with open("demofile.txt") as f:
    print(f.read()) 
#В этом случае вам не нужно беспокоиться о закрытии файла — оператор with сделает это автоматически.


f = open("demofile.txt")
print(f.readline())
f.close()


#Пример (чтение первых 5 символов):
with open("demofile.txt") as f:
    print(f.read(5))


#Вы можете прочитать одну строку с помощью метода readline():
with open("demofile.txt") as f:
    print(f.readline()) 

#Пример (чтение двух строк):
with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())

#Используя цикл for для перебора объекта файла, можно прочитать весь файл построчно:
with open("demofile.txt") as f:
    for x in f:
        print(x)
