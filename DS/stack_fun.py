stack=[]
def push():
    element=int(input("Enter the element:"))
    stack.append(element)
    print(stack)
def pop():
    if not stack:
        print("The stack is Empty!")
    else:
        e=stack.pop()
        print("The removed element:",e)
        print(stack)

while True:
    print("Select the operations to perform 1.push 2.pop 3.quit")
    choice=int(input())
    if choice == 1:
        push()
    elif choice ==2:
        pop()
    elif choice==3:
        break
    else:
        print("enter the crct operations")