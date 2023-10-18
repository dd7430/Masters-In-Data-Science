#what file handling means
# read, write, update and delete.

#writing a  file

r = "hi"

fp = open('demo_write.txt', 'w')
fp.write(r)
fp.close()

#reading a file

fp = open(r'C:\Users\USER PC\OneDrive\Desktop\Masters In Data Science\demo_write.txt', 'r')
print(fp.read())
fp.close()

#delete a file

import os

os.remove(r'C:\Users\USER PC\OneDrive\Desktop\Masters In Data Science\demo_write.txt')


#update a file

