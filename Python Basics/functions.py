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


#lambda function

x = lambda a,b: a + b
print(x(4,5))
print(x(10,11))

print(x("abhis","hek"))




#map, filter, reduce

#map

a = ['kholi', 'sachin', 'dravid']
print(a)

list_1 = map(str.upper,a)
print(list(list_1))


#filter

a = ['kholi', 'sachin', 'dravid']

def remove(x):
  return 'a' in x

print('a' in 'kholi')

list_2 = filter(remove,a)
print(list(list_2))


def even(x):
  if x % 2 == 0:
    return x

a = [1,2,3,4,5,6,7,8]
list2 = filter(even,a)
print(list(list2))

even1 = filter(lambda a : (a%2==0), array)
print(list(even1))

#reduce
a=[1,2,3,4,5,6]
from functools import reduce

lambda x,y : x+y

list_3 = reduce(lambda x,y: x+y, a)

print(list_3)


b = ['kholi', 'sachin', 'dravid']

from functools import reduce

lambda x,y : x + y

list_3 = reduce(lambda x,y: x +" plays next for " + y, b)

print(list_3)

