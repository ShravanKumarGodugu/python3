# Key word arguments

def sentence(name = 'Bucky', action = 'ate', item = 'Tuna'):
  print(name, action, item)


sentence()  # Returns Default values.
sentence('shravan', 'ate' , 'Oranges')
sentence(name = 'Wow', action = 'Yehi tho hai', item = 'Keyword_arguments')

