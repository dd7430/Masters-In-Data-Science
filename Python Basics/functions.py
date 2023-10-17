#simple function program

def add_1():
  a=1
  b=2
  c=a+b
  print(c)

add_1()


#cube of a number
def cubeNumber(x):
    return x**3
  
a = cubeNumber(3)

print(a)

def add_1():
  a=1
  b=2
  c=a+b
  print(c)

add_1() + 3 # error will show

#returning value

def add_2():
  a=1
  b=2
  c=a+b
  return c

print(add_2()+3) # program runs without errors
