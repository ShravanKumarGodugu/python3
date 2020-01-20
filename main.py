# Default arguments values :-\/

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
