Queue=[]
while True:
    print("\nContent--->>")
    print("\n1.Enqueue")
    print("\n2.Dequeue")
    print("\n3.Display")
    print("\n4.Exit")
    choice=int(input("Enter your choice(1-4): "))
    if(choice==1):
        a=int(input("\nEnter the element you want to insert: "))
        Queue.append(a)
    elif(choice==2):
        if(len(Queue)==0):
            print("underflow")
        else:
            p=Queue.pop(0)
            print("popped element =",p)
    elif(choice==3):
        if(len(Queue)==0):
            print("\nThe Queue is empty")
        else:
            print(Queue)
    elif(choice==4):
        print("\nExiting....")
        break
    else:
        print("\nInvalid Choice,Please Enter Correct choice")
