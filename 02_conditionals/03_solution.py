#Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60)
#1st Way
grade = int(input("My grade is : "))
if grade >= 90:
    print("A")
elif grade >=80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
# answer: My grade is : 55 , F (here u have to give input in interminal to get the grade)



#2nd way
# If your Score is mor than 100 
score = 90
if score >= 101:
    print("Please verify you grade again")
    exit() #To stop a program, u can normally use exit() or break
if score >= 90:
    grade = "A"
elif score >=80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("grade", grade) #grade A (here u have already assigned the score above)
