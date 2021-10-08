queue=[]
def enqueue():
    element=int(input("Enter the element:"))
    queue.append(element)
    print(queue)
def dequeue():
    if not queue:
        print("The queue is Empty!")
    else:
        e=queue.pop(0)
        print("The removed element:",e)
        print(queue)

while True:
    print("Select the operations to perform 1.push 2.pop 3.quit")
    choice=int(input())
    if choice == 1:
        enqueue()
    elif choice ==2:
        dequeue()
    elif choice==3:
        break
    else:
        print("enter the crct operations")