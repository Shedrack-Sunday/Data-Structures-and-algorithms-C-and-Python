#"1768. Merge Strings Alternately
#Create a merging empty array to return
# Get the minimum length to iterate
# Iterte using the minimum length, appending str1 and str2
#Add the remaining characters from the string using :
#Return a join of the merge string created


Def  Merge Strings Alternately(word1, word2)
     
    merge = []
    length = min(len(word1), len(word2))

    for i in range(length):
        merge.append(word1[i])
        merge.append(word2[i])


    merge += word1[length:]
    merge += word2[length:]

    return ''.join(merge)
