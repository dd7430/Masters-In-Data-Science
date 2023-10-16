s = (1,2,3,4,5)
print(s[1])

#In tuples once items are stored it is immutable
#Lists are mutable

#using list function a tuple can be changed into a list

d = list(s)
d[1] = "Zaheer"

print(d)

#turn list back to tuple

r = tuple(d)
print(r)
