a= input("Enter your word here : ")
b= input("Enter the character : ")
i=0
count=0

while(i<len(a)): 
   
 if (a[i] == b ) :
   count= count+1
 i=i+1 

print("The total no of time",b,"has occured = ", count ) 

    
 