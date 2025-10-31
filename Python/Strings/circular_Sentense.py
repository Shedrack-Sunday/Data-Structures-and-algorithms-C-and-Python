class Solution:
    def isCircularSentence(self, s: str) -> bool:
        arr = s.split()
        for i in range(len(arr)-1):
            if arr[i][-1] != arr[i+1][0]:
                return False
        
        return arr[-1][-1] == arr[0][0]
        
def isCircularSentence(sentence: str) -> bool:
    # Split the sentence into words
    words = sentence.split()
    
    # Loop through each word and check the conditions
    for i in range(len(words)):
        # Get the last character of the current word
        last_char = words[i][-1]
        # Get the first character of the next word, wrapping around with modulo
        first_char_next = words[(i + 1) % len(words)][0]
        
        # Check if the characters match
        if last_char != first_char_next:
            return False  # Not circular
    
    return True  # Circular if all conditions are met
