#Heapq provides implementation of Min heap
import heapq
heap=[]
heapq.heappush(heap,10)
heapq.heappush(heap,20)
heapq.heappush(heap,90)
heapq.heappush(heap,45)

print("HEAPPUSH OPERATION")
print(heap)

print("HEAPPOP OPERATION")
heapq.heappop(heap)
print(heap)

print("HEAPIFY OPERATION")
list=[1,11,20,3,45,64,13,2,21]
heapq.heapify(list)
print(list)

print("HEAPPUSHPOP OPERATION")
heapq.heappushpop(list,22)
print(list)

print("HEAPREPLACE OPERATION")
heapq.heapreplace(list,100)
print(list)

print("NSMALLEST OPERATION")
print(heapq.nsmallest(2,list))

print("NLARGEST OPERATION")
print(heapq.nlargest(3,list))