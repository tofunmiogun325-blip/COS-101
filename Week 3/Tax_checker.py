score = float(input("Enter Your Score:"))

if score < 0 or score > 100:
    print("Invalid Score")
elif score >= 50:
    print("You Passed!")
else:
    print("You Failed!")
