def cati(*args, sep="/"):
  print(sep.join(args))


cati("earth", "Mars", "Venus")
cati("earth", "Mars", "Venus", sep=".")