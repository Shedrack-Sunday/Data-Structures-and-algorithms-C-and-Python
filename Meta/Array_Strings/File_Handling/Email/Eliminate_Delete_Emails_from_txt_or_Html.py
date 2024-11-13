"""
Logic: Read words from input file(skip email), Write words to output file. rename output file.
0. Import re, os modules
1. Open output file fout in write mode.
2. Open input file in f in read mode and read every line
3. Create list of email addresses from line using re module
Example lst = ['a@test.com', 'b@test.com']
4. if word is not in list. Write into file
5. close both inupt, out files
6. Rename newly created file to old
Complexity
Time: n:words in input file. m:Emails in input file. O(mn)
Space: O(n+m): Creating a new file

"""

import re
import os

# Define input and output file names
input_filename = 'input.html'
output_filename = 'output.html'

# Open output file in write mode
with open(output_filename, "w") as fout:
    # Open input file in read mode
    with open(input_filename, "r") as fin:
        # Process each line in the input file
        for line in fin:
            # Find all email addresses in the current line
            list_email = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', line)
            
            # Write each email to the output file if it's not in list_email
            if not any(word in line for word in list_email):
                fout.write(line)

# Rename the output file to replace the input file
os.replace(output_filename, input_filename)
            
            
        
