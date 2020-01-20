def using_while(user_input):
  mtlist = [] # to store the value

  if user_input % 2 == 0:
    while user_input > 0:
      if user_input % 2 ==0:
        mtlist.append(user_input)
      user_input = user_input-1
  else:
    while user_input > 0:
      if user_input % 2 != 0:
        mtlist.append(user_input)
      user_input = user_input-1
  return mtlist

enput = int(input('Enter the range to print even or odd Numbers'))

calling_function = using_while(enput)

print("Output of the Given range {} ".format(calling_function))
