from collections import Counter

def top_3_words(filename):
    with open(filename, 'r') as f:
        words = f.read().split()

    word_counts = Counter(words)
    top_3 = word_counts.most_common(3)

    for word, count in top_3:
        print(f"{word}: {count}")

# Example usage:
filename = "paragraph.txt"
top_3_words(filename)







"""
Read the File and Count Words:

The with open(filename, 'r') as f: block opens the file in read mode.
The f.read().split() splits the file content into a list of words.
The Counter(words) creates a Counter object, which efficiently counts the occurrences of each word.
Find the Top k Words:

The nlargest(k, word_counts.items(), key=lambda item: item[1]) function returns a list of the k most common words and their counts.
Print the Top k Words:

The for loop iterates over the top k words and prints them along with their counts.
This approach is efficient and concise, making it a suitable solution for most text processing tasks.

"""
from collections import Counter
from heapq import nlargest

def top_k_words(filename, k):
    with open(filename, 'r') as f:
        words = f.read().split()

    word_counts = Counter(words)
    top_k = nlargest(k, word_counts.items(), key=lambda item: item[1])

    for word, count in top_k:
        print(f"{word}: {count}")

# Example usage:
filename = "paragraph.txt"
k = 3
top_k_words(filename, k)

"""
ime Complexity:

Reading the file: O(n), where n is the number of words in the file.
Creating the Counter object: O(n)
Using nlargest: O(n log k), where k is the number of top words to find. This is because nlargest uses a heap-based approach to efficiently find the top k elements.
Overall Time Complexity: O(n log k)

Space Complexity: O(n), to store the word_counts dictionary.

So, the provided Python solution has a time complexity of O(n log k) and a space complexity of O(n). This is efficient for most practical use cases

"""