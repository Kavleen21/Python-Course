base= int(input("Enter the number here : "))
expo= int(input("Enter the power here : "))

result=1 

if expo >=0 :
    for _ in range(expo):
        result*=base 
      
else: 
    for _ in range(-expo):
        result=1/result 

print(base,"raise to the power",expo,"is",result)