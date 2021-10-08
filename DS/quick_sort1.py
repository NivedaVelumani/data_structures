import statistics
def pivot_place(list,first,last):
    low=list[first]
    high=list[last]
    mid=(first+last)//2
    pivot_val=statistics.median([low,list1[mid],high])
    if pivot_val==low:
        pindex=first
    elif pivot_val == high:
        pindex=last
    else:
        pindex=mid
    list[last],list[pindex]=list[pindex],list[last]
    pivot=list[first]
    left=first+1
    right=last
    while True:
        while left<=right and list[left]<= pivot:
            left = left+1
        while left<=right and list[right] >=pivot:
            right=right-1
        if right<left:
             break
        else:
            list[left],list[right]=list[right],list[left]

    list[first],list[right]=list[right],list[first]
    return right

def quicksort(list,first,last):
    if first<last:
        p=pivot_place(list,first,last)
        quicksort(list,first,p-1)
        quicksort(list,p+1,last)

list=[45,32,24,64,12,34]
n=len(list)
quicksort(list,0,n-1)
print(list)
