s=input("Enter a string:")
y=[]
for a in s:
    if a not in y:
        y.append(a)
for b in y:
    n=s.count(b)
    print(b," ",n)
