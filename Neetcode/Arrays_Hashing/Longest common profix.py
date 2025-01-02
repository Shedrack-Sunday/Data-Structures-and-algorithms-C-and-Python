 def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]

time: O(n * m)
space: O(1)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = 0
        for i in range(len(strs[0])):
            curr_char = strs[0][i]
            for j in range(1, len(strs)):
                # The current string exhausts / encounter an unmatch character -> return immediately
                if i >= len(strs[j]) or strs[j][i] != curr_char:
                    return strs[0][:longest_prefix]
            longest_prefix += 1
        return strs[0][:longest_prefix] if longest_prefix else ""
