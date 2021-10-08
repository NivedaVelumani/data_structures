temp={}
temp['mon']=33.2
temp['tue']=34.5
temp['thurs']=33.2
temp['fri']=32.4
print(temp)
print(temp.keys())
print(temp.values())
print(temp['mon'])
print(len(temp))


#insert
dict1={1:45,2:34,3:67}
dict1[4]=90
dict1[1]=67
print(dict1)

#update
dict2={9:89,6:90}
dict1.update(dict2)
print(dict1)

#del
dict1={1:45,2:34,3:67}
del dict1[1]
print(dict1)
dict1.pop(2)
print(dict1)
