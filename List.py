L= []

I = int(input('enter a numbers'))

for i in range(I):
  M = int(input('Give Input'))
  L.append(M)
print (L)
L.reverse()
print (L)
L.sort()
print(L)
print(max(L),min(L))