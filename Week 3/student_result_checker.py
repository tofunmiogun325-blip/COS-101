name=input("Student Name: ")
course_score=float(input("Coursework score: "))
if course_score<0 or course_score>30:
    print("Score should be between 0 and 30")
    course_score=float(input("Coursework score: "))
    
exam_score=float(input("Examination Score: "))
if exam_score<0 or exam_score>70:
    print("Score should be between 0 and 70")
    exam_score=float(input("Examination Score: "))

total=course_score+exam_score

if total>=70:
    grade="A"

elif total>=60:
    grade="B"

elif total>=50:
    grade="C"

elif total>=45:
    grade="D"

elif total>=40:
    grade="E"

else:
    grade="F"

if total>=50:
    pass_status="Pass"

else:
    pass_status="Resit required"

#Output
print()
print("STUDENT RESULT SUMMARY")
print("Name: ",name)
print("Coursework Score: ",course_score,"/30")
print("Examination Score: ",exam_score,"/70")
print("Total: ",total,"/100")
print("Grade: ",grade)
print("Decision: ",pass_status)
    
