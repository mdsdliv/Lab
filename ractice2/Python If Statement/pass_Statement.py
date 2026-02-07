#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
#1
a = 33
b = 200

if b > a:
  pass 
# having an empty if statement like this, would raise an error without the pass statement

"""
pass — это заглушка в Python, которая ничего не делает, но нужна, чтобы блок кода не был пустым и не вызывал ошибку.
Код после pass продолжает выполняться как обычно.
Её используют временно или для синтаксической корректности пустых if, циклов или функций.
"""
#2
age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")

#3
score = 85

if score > 90:
  pass # This is excellent
print("Score processed")

#4
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")

#5
def calculate_discount(price):
  pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet
