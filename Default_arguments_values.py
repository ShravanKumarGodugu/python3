# Default arguments values :-\/
print("**** Example - 1 ****")
def ask_ok(prompt, retries = 4, complaint = 'Yes or No, Please..!'):
  while True:
    ok = input(prompt)
    if ok in ('Y', 'Ye', 'Yes'):
      return True
    if ok in ('n', 'no', 'nop', 'nope'):
      return False
    retries = retries - 1
    if retries < 0:
      raise IOError("refusenik user")
    print(complaint)
  
ask_ok("ENter Yes or NO")

print('\n')
#Example - 2

print("**** Example - 2 ****")

def get_gender(sex = 'Unknown'):
  if sex is 'm':
    sex = 'MALE'
  elif sex is 'f':
    sex = 'FEMALE'
  print(sex)


get_gender('m')
get_gender('f')
get_gender() # Prints default value which is assigned in the Function