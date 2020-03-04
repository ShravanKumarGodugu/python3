#  \\\ List Comprenhsion \\\

my_squares = []
for x in range(10):
  my_squares.append(x**2)
print(my_squares)


#  \\\ Simplification above of above written code \\\

my_squares = [x**2 for x in range(20)]
print(my_squares)


#  \\\ Using MAP function \\\

my_squares = list(map(lambda x: x**2, range(4)))
print(my_squares)


#  if and for conditions

my_squares = [(x,y) for x in [1,2,3] for y in [2,7,8] if x != y]
print(my_squares)