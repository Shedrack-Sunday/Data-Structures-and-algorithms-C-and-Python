- Substring Search
- Anagrams
- Palindromes
- Regular Expressions
- String Compression
- String Decompression
- String Matching
- String Parsing
- String Permutations
- String Reversal
- String Rotation
- String Segmentation
- String to Integer
- String to Double
- String to Long
- String to Lowercase
- String to Uppercase
- String to Title Case
- String Trimming
- String Tokenization
- String to Character Array
- Character Array to String
- Character Array to Integer
- Character Array to Double
- Character Array to Long


class Solution {
public:
    int longestValidParentheses(string s) {
        int n = s.size();
        int left = 0, right = 0;
        int maxLen = 0;
        
        for(int i = 0; i < n; ++i){
            if(s[i] == '('){
                ++left;
            }else{
                ++right;
            }
            
            if(right == left){
                maxLen = max(maxLen, 2*left);
            }else if(right > left){
                //more close than open
                left = right = 0;
            }
        }
        
        //traverse in reverse order
        left = right = 0;
        for(int i = n-1; i >= 0; --i){
            if(s[i] == '('){
                ++left;
            }else{
                ++right;
            }
            if(left == right){
                maxLen = max(maxLen, 2*left);
            }else if(left > right){
                //more close than open
                left = right = 0;
            }
        }
        
        return maxLen;
    }
};


// Longest Valid Parentheses
// Given a current working directory string, and the input to a cd command as a string, output the full path to /the new working directory.
//Simplified Path