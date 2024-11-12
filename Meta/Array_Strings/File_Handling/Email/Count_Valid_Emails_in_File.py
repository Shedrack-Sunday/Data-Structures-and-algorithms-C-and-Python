import re

def validEmails(fileName):
    valid_email = []
    Invalid_email = []
    
    valid_email_pattern = r'^[\w\._%+-]+@[\w.-]+\.[a-zA-Z]{2,}$'
    invalid_before_at = r'^[@]'
    invalid_between_at_and_dot = r'@\.'

    with open(fileName, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if re.match(valid_email_pattern, word):
                    valid_email.append(word)
                elif re.match(invalid_before_at, word) or re.search(invalid_between_at_and_dot, word):
                    Invalid_email.append(word)
                    
    print(f'Total invalid words: {len(Invalid_email)}')
    print(f'Total valid words: {len(valid_email)}')

# Example usage:
# validEmails('emails.txt')

                    
            
    
    