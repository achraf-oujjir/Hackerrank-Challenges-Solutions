class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLen = min(len(word1), len(word2))
        maxLen = max(len(word1), len(word2))
        result = ""
        for i in range(minLen):
            result += word1[i] + word2[i]

        if len(word1) == maxLen:
            result += word1[minLen:]
        else:
            result += word2[minLen:]

        return result
