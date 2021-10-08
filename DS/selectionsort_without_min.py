l1=[4,5,2,34,23,12,22]
for i in range(len(l1)-1):
    min_val=l1[i]
    for j in range(i+1,len(l1)):
        if l1[j]>min_val:
            min_val=l1[j]
    min_ind=l1.index(min_val,i)
    if min_val != l1[i]:
            min_val,l1[i]=l1[i],min_val
print(l1)


