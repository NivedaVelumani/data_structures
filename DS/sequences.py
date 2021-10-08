name="niveda"
list1=['n','i','v',33,3,23,31,1,1,11]
tuple1=(78,67,89,(28,90),90)
#length
print(len(name))
print(len(list1))
print(len(tuple1))

#slice
print(name[1:])
print(list1[2:4])
print(tuple1[1:4])

#count
print(name.count('n'))
print(list1.count(33))

#index
print(name.index('a'))

#lamba
lis=[9,7,4,55,33]
res=[x**2 for x in [3,4,2,21,1,12]]
print(res)

#membership
print('n' in name)
print('y' not in name)

#concatenation
s=" velumnai"
print(name+s)

list2=["nive","prani"]
print(list1+list2)

#minimum and maximum
list11=[9,89,78,47,489]
print(min(name))
print(min(list11))
print(max(name))
print(max(list11))

#sum
print(sum(list11))
