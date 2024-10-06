https://algo.monster/liteproblems/44



class Solution {
public:
    bool isMatch(const std::string& s, const std::string& p) {
        int strSize = s.size(), patternSize = p.size();
        // Create a DP table with dimensions (m+1) x (n+1) initialized to false.
        // dp[i][j] will be true if the first i characters of s match the first j
        // characters of p.
        std::vector<std::vector<bool>> dp(strSize + 1, std::vector<bool>(patternSize + 1, false));
      
        // The empty pattern matches the empty string.
        dp[0][0] = true;
      
        // Initialize the first row of the DP table. If we find '*', it can match 
        // an empty string, which is the state of dp[0][j-1].
        for (int j = 1; j <= patternSize; ++j) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 1];
            }
        }
      
        // Fill the DP table.
        for (int i = 1; i <= strSize; ++i) {
            for (int j = 1; j <= patternSize; ++j) {
                // If the characters match or the pattern character is '?',
                // we can transition from the state dp[i-1][j-1].
                if (s[i - 1] == p[j - 1] || p[j - 1] == '?') {
                    dp[i][j] = dp[i - 1][j - 1];
                } 
                // If the pattern character is '*', it can either match zero characters,
                // meaning we transition from dp[i][j-1], or it can match one character,
                // meaning we transition from dp[i-1][j].
                else if (p[j - 1] == '*') {
                    dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
                }
            }
        }
      
        // The final state dp[m][n] gives us the answer to whether the entire
        // strings s and p match with each other.
        return dp[strSize][patternSize];
    }
};