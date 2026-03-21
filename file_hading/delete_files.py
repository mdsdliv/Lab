#Удалить файл "demofile.txt":
import os
os.remove("demofile.txt")

#Проверить, существует ли файл, и затем удалить его:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("Файл не существует")

#Удалить папку "myfolder":
import os
os.rmdir("myfolder")
