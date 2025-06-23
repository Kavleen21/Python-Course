print("Half pyramid of floyd's triangle is : ")
a= int(input("Enter the number of rows here : "))

x=1
for i in range (a):
    for j in range (i+1):
     print(x, end=" ")
     x=x+1
    print()

    
