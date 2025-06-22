x= int(input("Enter first number here : "))
y= int(input("Enter second number here : "))
z= int(input("Enter third number here ; "))
 
temp=x
x=y
y=temp 
y=z 
z=temp 

print(x ,",",y,",",z)