globalVariable = 10

def sum():
  localVariable = 20
  global num 
  num = 2 
  print(localVariable)


sum()

print(num)