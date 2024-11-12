
"""
Count how many times A Single email address is found in file.
Example
[Input]
# cat a.txt
i am going to make it and that's i know soon amit@gmail.com I will prepare as per the role, vivek@gmail.com I know 
i need to stop think amit@gmail.com I will be my
own cheer leader. anil@gmail.com
And I know that's important amit@gmail.com to be motivated

[Output] 3
"""

import re

def email_count_occurences(filename, target_email):
    
    count = 0
    with open(filename, "r") as file:
        for line in file:
            email = re.finalall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', line)
            count += email.count(target_email)
    return count
            
            

    