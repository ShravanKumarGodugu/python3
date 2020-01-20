# Break Statement 

print('### Break Stement Execution ###')

for letter in 'Python':
  if letter == 'h':
    break
  print ('Current letter is - ', letter)
print ('\n')

var = int(input('Enter a Number'))
while var>0:
  var=var-1
  print('Current variable value is',var)
  if var==5:
    
    break
print ('End of Break Statement \n\n ')

print ('### Continue Statement ###')

for letter in 'Python':
  if letter =='h':
    continue
  print ('Current Letter Is == ',letter)

print ('\n')

var = int (input('Enter a Value'))
while var>0:
  var=var-1
  print('current value us - ',var)
  if var==5:
    continue
print ('End of continue Statement ')
