#  Another Example for Arbitrary Arguments.
# def cat(*args, sep = "/" ):
#   return sep.join(args)

# cat("earth", "Mars", "Venus")
# cat("earth", "Mars", "Venus", sep=".")

def make_increment(n):
  return lambda x:x+n

f = make_increment(int(input("Enter a no")))
print("Incremented no is {}".format(f(1)))