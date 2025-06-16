print("Select your ride :\n 1) Bike \n 2) Car ")
a= int(input("Enter your desired vehicle here : "))

if a==1 :
    print ("Type of bike :\n 1)Scooty \n 2)Scooter")
    b= int(input("Enter your desired bike choice here : "))

    if b==1 : 
     print ("You have selected Scooty ")
      
    else :
     print ("You have selected scooter ")

elif a==2 :
  print ("Type of car :\n 1) SUV \n 2)Sedan")
  c= int(input("Enter your desired car choice here : "))

  if c==1 :
    print ("You have selected SUV  ")

  else :
    print ("You have slected Sedan ")


else :
  print ("Wrong choice !")

