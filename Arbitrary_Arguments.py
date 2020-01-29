# Arbitrary Arguments (*)

def add_numbers(*args):
  total = 0
  for a in args:
    total += a
  print(total)

add_numbers(3)
add_numbers(3,51,20,22)