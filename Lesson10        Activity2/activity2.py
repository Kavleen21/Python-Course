lower= int(input("Enter the lower limit here : "))
upper= int(input("Enter the upper limit here : "))

print("Prime numbers between",lower,"and",upper,"are : ")

for num in range (lower,upper+1):
    if num >1:
     for i in range (2,num):
        if num%i == 0 :
           break 

     else :
       print(num)