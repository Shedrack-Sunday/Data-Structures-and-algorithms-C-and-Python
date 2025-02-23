def get_pattern(word):
    """
    Convert a word into a pattern where same letters are replaced with their first occurrence index.
    Example: 'mnnssnn' -> '011221'
    """
    pattern = []
    char_to_index = {}
    
    for i, char in enumerate(word):
        if char not in char_to_index:
            char_to_index[char] = len(char_to_index)
        pattern.append(str(char_to_index[char]))
    
    return ''.join(pattern)

def find_similar_patterns(words, target_word):
    """
    Find words from the list that have the same pattern as the target word.
    
    Args:
        words (list): List of words to search through
        target_word (str): Word to match pattern against
        
    Returns:
        list: Words that match the pattern of target_word
    """
    target_pattern = get_pattern(target_word)
    return [word for word in words if get_pattern(word) == target_pattern]

# Example usage
words = ["aabbcc", "aakkff", "akkffkk", "tjjiijj", "deftg"]
target = "mnnssnn"
result = find_similar_patterns(words, target)
print(f"Words with pattern similar to {target}: {result}")


"""



1. LeetCode 290 - "Word Pattern" (Easy)
   - Almost identical concept but reversed
   - Given pattern = "abba" and s = "dog cat cat dog", return true
   - This checks if pattern matches the string arrangement
   
2. LeetCode 205 - "Isomorphic Strings" (Easy)
   - Very similar concept
   - Given two strings s and t, determine if they are isomorphic
   - Example: "egg" and "add" are isomorphic (same pattern)
   - This is basically what we just did but comparing only two strings

3. LeetCode 890 - "Find and Replace Pattern" (Medium)
   - This is almost exactly the same as your question!
   - Given a list of words and a pattern, find all words that match the pattern
   - Example: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
   - Returns all words that follow same pattern as "abb"


"""
