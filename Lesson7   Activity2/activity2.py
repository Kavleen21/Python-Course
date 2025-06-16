a= int(input("Enter the number of units consumed here : "))

if a<50 :
 amount= a*2.60
 tax= 25 

elif a<=100 :
 amount= 130 + ( (a-50) * 3.25 )
 tax= 35 

elif a<=200 :
 amount= 130 + 162.50 + ((a-100)*5.26)
 tax= 45 

else :
 amount= 130 + 162.50 + 526 + ((a-200)*8.45)
 tax= 75 

total_amount= amount + tax 

print (total_amount )