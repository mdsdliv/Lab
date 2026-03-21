#     "a" — Добавление (Append) — добавляет данные в конец файла
#      "w" — Запись (Write) — перезаписывает всё существующее содержимое


with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

# открыть и прочитать файл после добавления:
with open("demofile.txt") as f:
  print(f.read())


with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

# открыть и прочитать файл после перезаписи:
with open("demofile.txt") as f:
  print(f.read())


f = open("myfile.txt", "x")
#Результат: создаётся новый пустой файл.
#Примечание: если файл уже существует, будет вызвана ошибка.
