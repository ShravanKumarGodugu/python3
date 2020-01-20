def fibonacci_series(given_number):
  a,b = 0, 1
  List = []
  while a < given_number:
    List.append(a)
    a, b = b, a+b
  return List

user = int(input('Enter the range to Print Fibonacci Series :-'))

add = fibonacci_series(user)

print("fibonacci_series Is === {}".format(add))