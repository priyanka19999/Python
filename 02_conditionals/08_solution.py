
#Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
#1st way
password = "Secure3P@982004"

if len(password) < 6:
    strength = "weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Strength of password is: ", strength)

# Ans: Strength of password is:  Strong


#2nd way (storing the length in a variable to avoid writing len(length) for multiple times )
length = "ggjjhjkbngc#gvhjjkh"
password_length = len(length)
if password_length < 6:
    password = "weak"
elif password_length <= 10:
    password = "Medium"
else:
    password = "Strong"
print(password)

# ans: Strong



