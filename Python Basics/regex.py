#regex (regular expression)


import re

a ="Hi Sachin, how are you doing? Sachin was born in Munbai"
print(a)

word = 'Sachin'

x = re.findall(word, a)
print(x)

y = re.search(word, a) 
print(y)

y.start(), y.end()

z = re.split(' ', a)

print(z)


password = 'abhi@sachin'

to_check = 'sachin'

u = re.match(password, to_check)

if u:
    print("match")
else:
    print("no match")