a= int(input("Enter the first speed here : "))
b= int(input("Enter the second speed here : "))
c= int(input("Enter the third speed here : "))

avg= (a+b+c)/3

print("The average speed is ",avg)

if avg>a and avg>b and avg>c :
     print(str(avg)+ " is greater than the speeds ", a,b,c )
 
elif avg>a and avg>b :
     print (str(avg)+ " is greater than speeds ",a,b)

elif avg>b and avg>c :
     print(str(avg)+" is greater than speeds ",b,c)

elif avg>c and avg>a :
     print(str(avg)+ " is greater than speeds ",c,a)

elif avg>a :
     print(str(avg)+" is just greater than ",a)

elif avg>b  :
     print(str(avg)+" is just greater than ",b)

elif avg>c :
     print(str(avg)+" is just greater than ",c)