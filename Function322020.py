def even():
  A = int(input('Enter a number'))
  
  if A%2==0:
    return "%d is even"%A
  else:
    return "{} is odd".format(A)
# print(even())
B = even()
print(B*3)

# if even() >0:
#   print ('hehehehe')
# else:
#   print ('ja ja revise kar ')
# return "Even"(A)