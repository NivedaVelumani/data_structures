list1=[3,4,32,22,77,23,2]
print("LIST OF ELEMENETS")
print(list1)

#Ascending order
for i in range(len(list1)-1):
    min_val=min(list1[i:])
    min_index=list1.index(min_val,i)  #duplicates values
    if list1[i] != list1[min_index]:  #if elements are present in its crcr pos no swap needed  
        list1[i],list1[min_index]=list1[min_index],list1[i]
print("SELECTION SORTING SORTED LIST ASCENDING ORDER")
print(list1)

#Descending Order
for i in range(len(list1)-1):
    max_val=max(list1[i:])
    max_index=list1.index(max_val,i) 
    if list1[i] != list1[max_index]:
        list1[i],list1[max_index]=list1[max_index],list1[i]

print("SELECTION SORTING SORTED LIST DESCENDING ORDER")
print(list1)