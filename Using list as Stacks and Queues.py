# Using List as Stack.
stack = [6,7,8,9]
stack.append(8)
stack.append(10)
print(stack)
stack.pop()
stack.pop()
print(stack)

# Using List as Queues(collection.deque).


from collections import deque
queue = deque(['shravan','shishir','adarsh'])
queue.append('Deepak')
queue.append('Abhilash')
print(queue)
queue.popleft()
print(queue)

