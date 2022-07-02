print("Restaurant")
print()
name = input("What is your Name ?\n")
print()
ques = input("Hello, " + name + " What would you like today ?\n")

if ques == "rice":
  print("Here is your Rice :)")
elif ques == "daal":
  print("Here is your daal :)")
elif ques == "roti":
  print("Here is your roti :)")
elif ques == "curry":
  print("Here is your curry :)")
elif ques == "chicken":
  print("Here is your chicken leg piece :)")
else:
  print("There is no item named " + ques + " in this Restaurant")
