# Arbitrary Arguments (*)

def add_numbers(*args):  # Using * we can take bunch of Args at a time
  total = 0
  for a in args:
    total += a
  print(total)

add_numbers(3)
add_numbers(3,51,20,22)  #  Taking Bunch of args at a time.