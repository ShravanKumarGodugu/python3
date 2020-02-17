# Using List as Stack.

print("---- Using List as Stack ---- \n")

stack = [6,7,8,9]
print("Basic LIST ===> ", stack)

stack.append(100)
stack.append(200)  # Last In 
print("\nUsing append method created List is  ===> ", stack)

# Using POP method
stack.pop()
print("\nUsing POP method(Retriving elements from a list (Last In First Out)  ===> ", stack)  #Last In First Out

stack.pop()
print("\nFinal Output Is ===> ", stack)

# Using List as Queues(collection.deque).

print("")

print("---- Using List as Queues(DEQUE) ----")
from collections import deque

queue = deque(['shravan','shishir','adarsh'])
print("Basic LIST ===> ", queue)


queue.append('Deepak')  # First In
queue.append('Abhilash')
print("\nUsing append method created List is  ===> ", list(queue))

# Using POP method

queue.popleft()
print("\nFinal output Using POP LEFT METHOD ===> ", list(queue))

queue.pop() 
print("\nUsing POP method(Retriving elements from a list (First In First Out) ===> ", list(queue)) # First Out

