import heapq


list1=[(1,"rio"),(4,"sio"),(3,"jio")]
heapq.heapify(list1)
for i in range(len(list1)):
    print(heapq.heappop(list1))