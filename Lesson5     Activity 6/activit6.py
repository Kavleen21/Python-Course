a= int(input("Enter your desired year here : "))

if a%4 == 0 and a%100 !=0 or a%400 == 0 :
    print ("The year is a leap year ")

else:
    print("The year is not a leap year ")