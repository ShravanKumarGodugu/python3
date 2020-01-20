# Buck_tutorial = Default values for Arguments:)

print("Default values for Arguments:)\n")


def get_gender(sex = 'Unknown'):
  if sex is 'm':
    sex = 'MALE'
  elif sex is 'f':
    sex = 'female'
  print (sex)


get_gender('m')
get_gender('f')
get_gender()

print('\n')

print("Variable Scope = Bucky Tutorial\n")

# Variable Scope = "Bucky Tutorial"

num = 143 # Is a Global variable it can be accessed where ever we want.


def hi():
  print(num)
  # If we assingned variable in a function it is can be used for that specific function only. Else we get error.


def bye():
  print(num)

hi()
bye()

print('\n')


# Keyword Arguments.
print("Keyword Arguments\n")

def dumb_sentence(name = 'Bucky', action = 'Ate', item = 'Tuna'):
  print(name,action,item)


dumb_sentence()
dumb_sentence('Sally', 'Farts', 'Gently')
dumb_sentence(item = 'Awesome')
dumb_sentence(item = 'Awesome', action = 'Is')


