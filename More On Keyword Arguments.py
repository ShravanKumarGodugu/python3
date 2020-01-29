# Another Example of Keyword Arguments.
def parrot(voltage='1', state='a Stiff', action='voom', type1='Norwegian Blue'):
  print("--This Parrot wouldn't", action)
  print("if you put ", voltage, "Volts Through it.")
  print("-- lovely Plumage, the ", type1)
  print("-- It's", state, ":")


parrot()                              # Its returns Default value of argumets
parrot(2000)                          # Positional Argument
parrot(voltage='3000')                # Keyword Argument
parrot(voltage='4000', action='voom') # Keyord Argument
parrot('a Million', 'Brief of life', 'Jump') # Positional Argument
parrot('A thousand ', state='Pushing up the daisies') # Key & Positional Arguments