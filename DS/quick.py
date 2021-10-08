import random

def pivot_place(list,first,last):
    rindex=random.randint(first,last)
    list[rindex],list[last]=list[last],list[rindex]
    pivot=list[last]
    left=first
    right=last-1
    while True:
        while left<=right and list[left]<= pivot:
            left = left+1
        while left<=right and list[right] >=pivot:
            right=right-1
        if right<left:
             break
        else:
            list[left],list[right]=list[right],list[left]

    list[last],list[left]=list[left],list[last]
    return left

def quicksort(list,first,last):
    if first<last:
        p=pivot_place(list,first,last)
        quicksort(list,first,p-1)
        quicksort(list,p+1,last)

list=[45,32,24,64,12,34]
n=len(list)
quicksort(list,0,n-1)
print(list)
