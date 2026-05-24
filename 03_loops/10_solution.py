#Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time
wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1 , "- wait" , wait_time, )
    
    time.sleep(wait_time)
    wait_time *= 2
    attempts +=1 

# ANS:
# Attempt 1 - wait 1
# Attempt 2 - wait 2
# Attempt 3 - wait 4
# Attempt 4 - wait 8
# Attempt 5 - wait 16