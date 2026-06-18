file = open("youtube.txt", "w")

try:
    file.write("chai aur code")
finally:
    file.close()

#Explanation
# Open youtube.txt in write mode ("w").
# Write "chai aur code" into the file.
# No matter what happens, execute file.close(). 
    
with open("youtube.txt", "w") as file:
    file.write("chai aur python")
    
#Explanation 
# Open the file.
# Assign it to file.
# Run the code inside the block.
# Automatically close the file when the block ends.