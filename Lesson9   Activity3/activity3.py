a= int(input("Entter the number here : "))

sum=0 
temp=a

while temp>0 :
    digit= temp%10 
    sum=sum+ digit**3
    temp=temp//10 

if sum==a :
    print("It is an armstrong number")

else:
    print("It is not an armstrong number")