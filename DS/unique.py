def catch_unique(list_in):
   # intilize an empty list
   unq_list = []

   # Check for elements
   for x in list_in:
      # check if exists in unq_list
      if x not in unq_list:
         unq_list.append(x)
         # print list
   for x in unq_list:
      print(x)

Alist = ['Mon', 'Tue', 'Mon', 'wed', 40, 40]
print("Unique values from the list is")
catch_unique(Alist)









#duplicate
# my_list = [1,2,2,3,1,4,5,1,2,6]
# myFinallist = []
# for i in my_list:
#     if i not in myFinallist:
# myFinallist.append(i)
# print(list(myFinallist))