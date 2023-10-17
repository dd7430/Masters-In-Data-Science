#list
 #Creating a List
a = ["Abishek", 1, 10.5, True, [1,2,3,4,5]] 

print(a)

#using variables in lists
z = "Zaheer"
a = ["Abishek", 1, 10.5, True, [1,2,3,4,5], z ] 

#Printing particular elements in a list or aka Indexing.

print(a[2])

print(a[-1])

print(a[4])
 #slicing 

print(a[0:2])

#slicing until the list ends

b = [1,2,10,23,41,62,80,91]
print(b[2 : ])

#reversing the list
b.reverse()
print(b)

print(b[::-1]) 

#replacing the items in a list

b[1]= "Puneeth"
print(b)

#appending

a = [1,2,3,4,5]
a.append(10)
print(a)
