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

#using def to create variables inside def
def add_2(a,b):
  c=a+b
  print c

add_2(5,10)


#local and global variables

a = 10 #global variable
def cat():
  c='virat'
  print c

print c # c will not print because it is a local variable inside the function. Without calling the function you cannot print 'virat'

#giving values for variables inside the def function

def add_2(a=5,b=20):
  c=a+b
  print (c)

add_2()
add_2(12,11) # if values are given to the variables it uses the new values if written by the def function. 
  
