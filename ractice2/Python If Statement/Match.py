"""Вместо того чтобы писать много if..else, можно использовать match.
match выбирает один из нескольких блоков кода для выполнения."""

#1
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

#2Используйте символ подчёркивания _ в последнем case, если хотите, чтобы блок кода выполнялся, когда нет других совпадений.

day = 4
match day:
    case 6:
        print("Сегодня суббота")
    case 7:
        print("Сегодня воскресенье")
    case _:
        print("Жду выходных")

#3 Используйте символ | как оператор или в case, чтобы проверять несколько значений в одном случае.

day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Сегодня будний день")
    case 6 | 7:
        print("Я люблю выходные!")

#4You can add if statements in the case evaluation as an extra condition-check:

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")

#5
fruit = "apple"
color = "green"

match fruit:
    case "apple" if color == "red":
        print("Красное яблоко")
    case "apple" if color == "green":
        print("Зелёное яблоко")
    case "banana":
        print("Банан")
    case _:
        print("Другое фрукт")
