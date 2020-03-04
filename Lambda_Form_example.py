# LAMBDA FORM EXAMPLE

def make_increment(n):
  return lambda x:x+n


f = make_increment(int(input("Enter a no")))
print("Incremented no is {}".format(f(1)))


