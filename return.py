# return

def minor_major(AGE):
  minor_age = None
  major_age = None

  if AGE > 21:
    major_age = AGE
    minor_age = 0
    return major_age,minor_age
  
  else:
    major_age = 0
    minor_age = AGE
    return major_age,minor_age

A = int(input("Enter the AGE"))
major,minor = minor_major(A)

if major:
  print ("Major", major)
else:
  print ("Minor", minor)