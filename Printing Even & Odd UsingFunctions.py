def even_and_odd_printer(number):

  evenList = []
  oddList = []

  for i in range(1,number+1):
    if i % 2 == 0:
      evenList.append(i)

    else:
      oddList.append(i)
  return evenList, oddList
  
user = int(input('Enter the range to print Even & Odd Numbers'))
a, b = even_and_odd_printer(user)

print ('Even List is {} \nOdd List is{}'.format(a,b))
