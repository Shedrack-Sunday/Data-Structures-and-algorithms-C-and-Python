
"""
Programming: 1. There are some fortune sentences in a file, and the delimiter is a line of '#', e.g.
abc
#
abc,
def
#
output a fortune sentence randomly, and if it is multiple lines, merge them into one line. Additional: What to do if the file is very large, I don't know how to get the random number in, so I just wrote how to process a large file..
"""

import random

def get_random_fortune(filename):
    with open(filename, 'r') as file:
        fortune = []
        curr_words = []
        for line in file:
            line = line.strip()
            if line == '#':
                if curr_words:
                    fortune.append(" ".join(curr_words))
                    curr_words = []
            else:
                curr_words.append(line)  
     
         
        if curr_words:
            fortune.append("".join(curr_words)) 
            
        if fortune:
            return random.choice(fortune)


random_file = "example.txt"
print(get_random_fortune(random_file))
        