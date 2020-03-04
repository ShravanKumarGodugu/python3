L =[]
condition = 'y'
while [1]:
  A=int(input('Enter Number'))
  L.append(A)
  print (L)
  condition = input('Do you want to enter more no. Type y for yes and n for no')
  if condition == 'y':
    continue
  elif condition == 'n':
    break
print (L)

