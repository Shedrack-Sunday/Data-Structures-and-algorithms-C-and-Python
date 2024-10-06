https://algo.monster/liteproblems/408



class Solution {
public:
    bool validWordAbbreviation(string word, string abbr) {
        int wordIndex = 0, abbrIndex = 0; // Initiate indices to iterate over word and abbreviation strings
        int wordLength = word.size(), abbrLength = abbr.size(); // Get lengths of both word and abbreviation

        // Iterate over the entire word to check if it matches with abbreviation
        while (wordIndex < wordLength) {
            if (abbrIndex >= abbrLength) {
                return false; // If abbreviation is shorter than the word part processed, return false
            }

            // If the current characters match, move to the next character in both strings
            if (word[wordIndex] == abbr[abbrIndex]) {
                ++wordIndex;
                ++abbrIndex;
                continue;
            }

            // Find the next non-digit character in abbreviation to extract the numeric part
            int numStart = abbrIndex;
            while (numStart < abbrLength && isdigit(abbr[numStart])) {
                ++numStart;
            }

            // Get the numeric part as a substring
            string numStr = abbr.substr(abbrIndex, numStart - abbrIndex);

            // If there's no numeric part or it starts with a zero, the abbreviation is invalid
            if (numStart == abbrIndex || numStr[0] == '0') {
                return false;
            }

            // Convert numeric string to integer
            int num = stoi(numStr);
          
            // Advance the word index by the numeric value and update the abbreviation index
            wordIndex += num;
            abbrIndex = numStart;
        }

        // After processing, both indices should be at the end of their respective strings
        return wordIndex == wordLength && abbrIndex == abbrLength;
    }
};