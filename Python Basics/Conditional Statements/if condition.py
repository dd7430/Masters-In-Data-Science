#Basic IF conditional statement
a = int(input("Enter your marks: "))

if a>=35:
  print("Pass")
else:
  print("Fail")


#Using elif condition
a = int(input("Enter your marks: "))

if a>90:
  print("Topper")
elif a>60:
  print("First Class")
elif a>=35: #multiple elif can be used
  print("Just Pass")
else:
  print("Fail")

#nested if (a if condition inside a if condition)

a = int(input("Enter the marks: "))
subject = input("Enter the subject: ")

if subject =="Maths":
  if a>90:
    print("Topper")
  elif a>60:
      print("First Class")
  elif a>=35: #multiple elif can be used
      print("Just Pass")
  else:
    print("Fail")
else:
  print("Not here")
