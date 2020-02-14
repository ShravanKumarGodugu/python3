#  Sentinel controlled repetition
empty_list = []

while True:
  a= input("Do you want to enter the items in the list?(y for yes n for no)\n:")
  if a == 'y':
    x = input("Enter the item\n:")
    empty_list.append(x)
  else:
    break
print("Items you have entered are:- \n\n{}".format(empty_list))

print("\n")

# Adding List Functions

empty_list.append(1) # Append method
print("Using 'APPEND' method", empty_list)
print("\n")

empty_list.extend(['s','h','r','a','v','a''n']) #  To append a list of elements.
print("Using EXTEND Method ",empty_list)
print("\n")

empty_list.insert(3,'chutiya') #  Insert an item at a given Position.
print("Using INSERT METHOD",empty_list)
print("\n")

empty_list.remove('chutiya') #  Remove the item from the list which is defined else will get an error.
print("Using REMOVE Method",empty_list)
print("\n")

empty_list.pop(5) #  Remoce the item at the given possition. If Possition is not specified it removes the last item in the list.
print("Using Pop method",empty_list)
print("\n")

empty_list.count(a) #  Returns the number of times 'a' appears in the list. Else
print('\n',empty_list)



# INDEX example
mylist = [2,4,1,5,6]
print("My List IS",mylist)
B = mylist.index(1)
print("index of '1' : ", B)
