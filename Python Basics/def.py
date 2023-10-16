def cubeNumber(x):
    return x**2
 
 
  
a = cubeNumber(3)

print(a)





def getsome(a, b, c):
    return a+b+c

print(getsome(1,7,9))


# return function returns the value before printing



#Combine Name

#def combineName(first , middle, last):
#    return first + " " +middle + " " + last

#fullname= combineName("Danvanth", "Darshan", "Poovanalingam")
#print(fullname)


def combineName(first , middle, last):
    return first + " " +middle[0:7] + " " + last

fullname= combineName("Danvanth", "Darshan", "Poovanalingam")
print(fullname)