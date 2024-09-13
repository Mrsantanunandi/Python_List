stack=[]

while True:
    print("Enter a choice: ")
    print("\n1. Push")
    print("\n2. Pop")
    print("\n3. peep")
    print("\n4. Display")
    print("\n5. Exit")
    choice=int(input("Enter your choice(1-5): "))
    if(choice==1):
        a=int(input("Enter the item you want to insert:"))
        stack.append(a)
    elif(choice==2):
        if(len(stack)==0):
            print("\nThe Stcak is empty")
        else:
            x=stack.pop()
            print(f"The poped item is {x}")
    elif(choice==3):
        if(len(stack)==0):
            print("\nThe Stcak is empty")
    elif(choice==4):
        w=stack
        print("The Stack is: ",w)
    elif(choice==5):
        print("\nExiting...")
        break
    else:
        print("Invalid Choice")


                
        
                     
