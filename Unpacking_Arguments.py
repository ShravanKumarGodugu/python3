# Unpacking_Arguments (Bucky's Example).

def health_calculator(age, apples_ate,cigarates_smoked):
  answer = (100-age) + (apples_ate * 3.5) - (cigarates_smoked * 2 )
  print(answer)


bdata = [27,20,0]
health_calculator(bdata[0], bdata[1], bdata[2])
health_calculator(*bdata)


# Example2


def parrot(voltage, state='A Stiff', action='Voom'):
  print("--This parrot wouldn't ", action), print("If u Put",voltage,'Volts through it'), print("E's", state, "!")


d = {"voltage": "Four Million", "state": "Bleedin' Demissed", "action": "VOOM"}
parrot(*d)


# Example 3:


def a():
  args = [3,6]
  return args

print(list(range(*a()))) # In Python 3 Range is an object


