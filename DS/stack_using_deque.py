# import collections
# stack=collections.deque()
# stack.append(12)
# stack.append(10)
# stack.append(78)
# print(stack)
# stack.pop()
# print(stack)


import queue
stack=queue.LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)
stack.put(40,timeout=1)
print(stack)