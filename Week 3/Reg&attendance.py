registration_status=input("Registration Complete? Enter yes or no: ")
if registration_status==registration_status.lower():
    attendance=float(input("Enter attendance percentage: "))
    if registration_status=="yes" and attendance>=75:
        print("You can participate in the practical assessment")
    else:
        print("You cannot participate in this assessment")
        
else:
    print("Value should be in lower case")
