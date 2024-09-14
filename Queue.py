Queue=[]
front=-1
rear=-1
while True:
    print("\nContent--->>")
    print("\n1.Enqueue")
    print("\n2.Dequeue")
    print("\n3.Display")
    print("\n4.Exit")
    choice=int(input("Enter your choice(1-4): "))
    if(choice==1):
        a=int(input("\nEnter the element you want to insert: "))
        if(front==-1 and rear==-1):
            front=rear=0
            Queue.append(a)
        else:
            rear=rear+1
            Queue.append(a)
    elif(choice==2):
        if(front==-1 and rear==-1):
            print("\nQueue Underflow...")
        elif front == rear:
            y = Queue.pop(front)
            print("\nThe Poped item is: ", y)
            front = rear = -1
        else:
            y=Queue.pop(front)
            print("\nThe Poped item is:  ",y)
            front=front+1
    elif(choice==3):
        if(front==-1 and rear==-1):
            print("\nThe Queue is empty")
        else:
            print(Queue)
    elif(choice==4):
        print("\nExiting....")
        break
    else:
        print("\nInvalid Choice,Please Eneter Correct choice")