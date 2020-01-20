# tutorial Point example for return statement

def addition(arg1,arg2):
  # add both the Parameters and the same.

  t = arg1 + arg2
  print('Inside the Function :',t)
  return t 

# Now we can call the Function.

t = addition(20,30)
print ('Outside the Function :',t)




# Scope of Variables ( Global vs Local variables)

total = 0 #This is a Global variable

# Function Definition is here.

def adding(a,b):
  # adding both the Parameters and return them.
  total = a+b
  print ("Insid the function Local total :", total)
  return total
# Now we can call the function,
adding (22,33)
print ("Outside the function Global total :", total)