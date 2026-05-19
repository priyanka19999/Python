#Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).
age = 25
if age < 13:
    print("child")
elif age <20:
    print("teenager")
elif age <60:
    print("Adult")
else :
    print("senior")
# ans: Adult


#Vote eligibility
age = int(input("your age :"))
if age >= 18:
    print("Eligible for vote")
else:
    print("Not eligible")
#your age: 20 // eligible for vote