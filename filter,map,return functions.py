# Funtional Programing Tools ::


# FILTER Function
def f(x):
    return x % 2 != 0 and x % 3 != 0


calling = filter(f, range(2, 25))
print("Using FILTER FUNCTION(Returns List of values) ====>", list(calling))

# MAP function

def cube(y):
  return y*y*y

calling_map = map(cube, range(1,10))
print("Map function Output Is (Returns list of values) ", list(calling_map))


#  REDUCE FUNCTION

from functools import reduce
def my_sum(x,y):
  return x+y


calling_reducefuntion = reduce(my_sum, range(2,20))
print("Reduce function Output is (Renturns single value)", calling_reducefuntion)
