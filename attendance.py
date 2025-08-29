medicalcause = input("Please enter your medical cause YES or NO")
attendance = int(input(" Pease enter your attendance"))
if medicalcause == "yes":
    print(" YES you are allowed")
    
else :
    if attendance > 75:
        print("You are allowed cause you attendance more than 75 % ")
    else :
        print("You are not allowed")