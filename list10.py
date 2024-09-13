values=[]# a list of values
#input 10 values from user
print("Enter 10 in: ")
for i in range(10):
    new_value=int(input((i+1)))
    values+=[new_value]
print("\nCreating a histogram from, the values: ")
print("%s %10s %10s" %("Element" , "value","Histogram"))
for i in range(len(values)):
      print("%7d %10d %s" %(i,values[i],"*"*values[i]))
